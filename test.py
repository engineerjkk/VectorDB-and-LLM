from openai import OpenAI
from config import MY_OPENAI_API_KEY, MY_IMG_MODEL

def test_openai_api():
    # 클라이언트 초기화
    client = OpenAI(api_key=MY_OPENAI_API_KEY)

    try:
        # 간단한 API 요청 보내기
        response = client.chat.completions.create(
            model=MY_IMG_MODEL,
            messages=[
                {"role": "user", "content": "Hello, OpenAI!"}
            ]
        )
        
        # 응답 확인
        if response.choices[0].message.content:
            print("API 테스트 성공!")
            print("응답:", response.choices[0].message.content)
            return True
        else:
            print("API 응답이 비어 있습니다.")
            return False

    except Exception as e:
        print(f"오류 발생: {str(e)}")
        return False

if __name__ == "__main__":
    test_openai_api()