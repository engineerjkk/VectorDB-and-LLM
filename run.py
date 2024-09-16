import streamlit as st
import openai
import os
from setup_req import setup
import requests
from PIL import Image
import io
from io import BytesIO
import base64
from search_method_wrapper import text_input_only, image_input_only, hybrid_input, create_modifications
from config import MY_OPENAI_API_KEY, MY_IMG_MODEL
st.set_page_config(layout="wide")
# Custom CSS for minor styling improvements
st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
    }
    .stTextInput > div > div > input {
        background-color: #f1f1f1;
    }
    .app-title {
        font-size: 2rem;
        font-weight: bold;
        color: #1E90FF;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
</style>
""", unsafe_allow_html=True)

# Setup. 필요한 모델과 localDB를 한 번에 upload
@st.cache_resource(show_spinner=True)
def cached_setup():
    print("Reading necessary files.")
    return setup()

pc, index, clip_model, clip_processor, \
    clip_tokenizer, splade_model, splade_tokenizer, \
        local_db, yolo_feature_extractor, yolo_model = cached_setup()

# Initialize openai api
os.environ['OPENAI_API_KEY'] = MY_OPENAI_API_KEY
openai.api_key = os.environ["OPENAI_API_KEY"]

# Display an image at the top of the app, fully extended width-wise
st.image("banner.jpg", use_column_width=True)

# App title
st.markdown('<p class="app-title">VectorDB와 LLM 기반 상품 검색+추천 시스템</p>', unsafe_allow_html=True)

# Function to add logs to the markdown field
def add_log(logs, new_log):
    logs.append(new_log)
    return logs

# Placeholders for displaying logs in the main section
log_placeholder1, log_placeholder2 = st.empty(), st.empty()

# Initialize image_paths
image_paths = []

# Define the sidebar tabs
tab1, tab2 = st.sidebar.tabs(["상품 검색", "패션 생성"])

# Tab 1: 상품 서치 - StyleFinder
with tab1:
    st.header("상품 검색")
    text_input1 = st.text_area("찾고자 하시는 상품을 입력해 주세요.              \n"
                               "(사진 첨부시, 텍스트는 분위기적으로 입력해주세요. \n"
                               "예) 따뜻한 느낌으로 찾아줘)", 
                               key="search_text", 
                               height=200)
    image_input1 = st.file_uploader("찾고자 하시는 상품 사진을 첨부해 주세요", type=["jpg", "png"], key="search_image")
    top_k = st.number_input("몇개의 상품을 보여드릴까요?", min_value=1, max_value=20, value=5, step=1, key="top_k")
    
    logs1 = []
    if st.button("검색하기", key="search_btn"):
        if text_input1 and image_input1:
            logs1 = add_log(logs1, f"Text and image received.\nText: {text_input1}")
            image = Image.open(image_input1)
            result = hybrid_input(text_input1, image, index, yolo_feature_extractor, yolo_model, clip_model, clip_tokenizer, clip_processor, local_db, splade_model, splade_tokenizer, openai.api_key, top_k)
            if result:
                log, image_paths = result
                for i, item in enumerate(["Detected_items", "image_Descriptions", "search_text", "원하는 분위기"]):
                    logs1 = add_log(logs1, f"{item}: {log[i]}")
            else:
                logs1 = add_log(logs1, "Nothing found")
        elif text_input1 or image_input1:
            if text_input1:
                logs1 = add_log(logs1, f"입력하신 내용 : {text_input1}")
                result = text_input_only(text_input1, index, clip_model, clip_tokenizer, splade_model, splade_tokenizer, top_k=top_k)
                if result:
                    _, image_paths = result
            if image_input1:
                image = Image.open(image_input1)
                result = image_input_only(image, index, yolo_feature_extractor, yolo_model, clip_model, clip_tokenizer, clip_processor, splade_model, splade_tokenizer, local_db, openai.api_key, top_k)
                if result:
                    log, image_paths = result
                    logs1 = add_log(logs1, "Image received.")
                    for i, item in enumerate(["Detected_items", "image_Descriptions", "search_text"]):
                        logs1 = add_log(logs1, f"{item}: {log[i]}")
                else:
                    logs1 = add_log(logs1, "No fashion item detected.")
        else:
            logs1 = add_log(logs1, "Please provide at least one input.")
        
        log_messages1 = "\n".join(f"- {log}" for log in logs1)
        log_placeholder1.markdown(log_messages1)

# Tab 2: 패션 추천 - StyleFinder
with tab2:
    st.header("패션 생성")
    text_input2 = st.text_area("이미지를 업로드하시고 원하시는 패션 분위기를 입력해주세요.", key="recommend_text", height=200)
    image_input2 = st.file_uploader("참고할 수 있는 이미지를 업로드해주세요.", type=["jpg", "png"], key="recommend_image")
    if st.button("패션 생성하기", key="recommend_btn"):
        if text_input2 and image_input2:
            image = Image.open(image_input2)
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format=image.format)
            base64_image = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            result = create_modifications(text_input2, base64_image, openai.api_key)
            if result:
                log, image_url = result
                response = requests.get(image_url)
                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content))
                    st.image(image, caption='Generated Image')
                else:
                    st.error('Failed to fetch image. Please check the URL.')
            else:
                log_placeholder2.markdown("- Please provide fashion-related text")    
        else:
            log_placeholder2.markdown("- Please provide text and image input.")

# Display uploaded images
for input_image, label in [(image_input1, "Search"), (image_input2, "Style reference")]:
    if input_image:
        st.markdown(f"Uploaded {label} image:")
        st.image(Image.open(input_image), caption=f'Uploaded {label} Image.', use_column_width=True)

# Display search results
if image_paths:
    st.subheader("검색 결과")
    for k, v in image_paths.items():
        st.write(k)
        cols = st.columns(len(v))
        for col, img_path in zip(cols, v):
            with col:
                st.image(img_path)