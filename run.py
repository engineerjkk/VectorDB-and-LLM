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
# Initialize image_paths and generated_image
image_paths = []
generated_image = None

# Define the sidebar tabs
st.sidebar.markdown("Designed by 강준구")
st.sidebar.markdown("""
## 상품 검색 및 패션 생성 시스템

이 애플리케이션은 두 가지 주요 기능을 제공합니다:

1. **상품 검색**: 텍스트나 이미지를 사용하여 원하는 패션 아이템을 검색합니다.
2. **패션 생성**: AI를 활용하여 새로운 패션 스타일을 생성합니다.

아래 탭을 선택하여 원하는 기능을 사용해보세요.
""")
tab1, tab2 = st.sidebar.tabs(["상품 검색", "패션 생성"])

# Tab 1: 상품 서치 - StyleFinder
with tab1:
    st.header("상품 검색")
    text_input1 = st.text_area("찾고자 하시는 상품을 입력해 주세요.              \n"
                               "(사진도 함께 첨부하실 경우, 텍스트는 분위기적으로 입력해주세요. \n"
                               "예) 따뜻한 느낌으로 찾아줘)", 
                               key="search_text", 
                               height=200)
    image_input1 = st.file_uploader("찾고자 하시는 상품 사진을 첨부해 주세요", type=["jpg", "png"], key="search_image")
    top_k = st.number_input("몇개의 상품을 보여드릴까요?", min_value=1, max_value=20, value=5, step=1, key="top_k")
    
    logs1 = []
    st.sidebar.markdown("시간이 너무 오래걸릴 경우, 텍스트를 변경해 다시 시도바랍니다.")
    if st.button("검색하기", key="search_btn"):
        with st.spinner('검색 중...'):
            if text_input1 and image_input1:
                logs1 = add_log(logs1, f"Text and image received.\nText: {text_input1}")
                image = Image.open(image_input1)
                result = hybrid_input(text_input1, image, index, yolo_feature_extractor, yolo_model, clip_model, clip_tokenizer, clip_processor, local_db, splade_model, splade_tokenizer, openai.api_key, top_k)

                if result:
                    log, image_paths = result
                    #for i, item in enumerate(["Detected_items", "image_Descriptions", "search_text", "원하는 분위기"]):
                    #    logs1 = add_log(logs1, f"{item}: {log[i]}")
                else:
                    #logs1 = add_log(logs1, "다시 입력해주세요. 상품명보다는 분위기적으로 입력해주시면 감사하겠습니다. ")
                    st.warning("**다시 입력해주세요. 상품명보다는 분위기적으로 입력해주시면 감사하겠습니다.**")
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
                        #for i, item in enumerate(["Detected_items", "image_Descriptions", "search_text"]):
                        #    logs1 = add_log(logs1, f"{item}: {log[i]}")
                    else:
                        logs1 = add_log(logs1, "해당 상품은 없는 상품입니다.")
            else:
                logs1 = add_log(logs1, "텍스트 입력 또는 이미지를 첨부해주세요.")
        
        #log_messages1 = "\n".join(f"- {log}" for log in logs1)
        #log_placeholder1.markdown(log_messages1)

# Tab 2: 패션 추천 - StyleFinder
with tab2:
    st.header("패션 생성")
    text_input2 = st.text_area("이미지를 업로드하시고 원하시는 패션 분위기를 입력해주세요.", key="recommend_text", height=200)
    image_input2 = st.file_uploader("참고할 수 있는 이미지를 업로드해주세요.", type=["jpg", "png"], key="recommend_image")
    if st.button("패션 생성하기", key="recommend_btn"):
        with st.spinner('이미지 생성 중...'): 
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
                        generated_image = Image.open(BytesIO(response.content))
                    else:
                        st.error('Failed to fetch image. Please check the URL.')
                else:
                    st.markdown("- Please provide fashion-related text")    
            else:
                st.markdown("- Please provide text and image input.")

# Display results in the main area
if tab1:
    # Display uploaded image for search
    if image_input1:
        st.markdown("### 업로드된 검색 이미지:")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(Image.open(image_input1), caption='Uploaded Search Image', width=300)

    # Display search results
    if image_paths:
        st.markdown("---")  # 구분선 추가
        st.subheader("검색 결과")
        for k, v in image_paths.items():
            #st.write(k)
            st.markdown(f"#### {k}") 
            cols = st.columns(len(v))
            for col, img_path in zip(cols, v):
                with col:
                    st.image(img_path, width=300)

if tab2:
    # Display uploaded image for style reference
    if image_input2:
        st.markdown("### 업로드된 스타일 참조 이미지:")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(Image.open(image_input2), caption='Uploaded Style Reference Image', width=300)
    
    # Display generated image
    if generated_image:
        st.markdown("---")  # 구분선 추가
        st.subheader("생성된 이미지")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(generated_image, caption='Generated Image', width=300)