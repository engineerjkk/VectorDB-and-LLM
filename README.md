# 벡터DB와 LLM 기반 상품 검색 및 추천 시스템
# [웹 페이지 바로가기](http://34.47.106.54:8501/)  
(가끔 서버가 불안정하여 접속이 안될 때가 있습니다. engineerjkk@naver.com 으로 메일 주시면 열어드리겠습니다.)  

## 프로젝트 개요

- **기간**: 4개월 (2024-05 ~ 2024-08)
- **유형**: 개인 프로젝트
- **역할**: 벡터DB와 LLM 기반 상품 검색 및 추천 시스템 개발자

### 목적
Deep Metric Learning 및 이미지 검색에 관한 석사 연구 경험을 확장하여, LLM을 활용한 상품 검색 및 추천 시스템 개발

## 핵심 기능

- 텍스트 및 이미지 형태의 쿼리 처리 및 임베딩 생성
- 고차원 벡터 공간에서의 효율적 유사도 기반 검색
- 개인화된 상품 추천 알고리즘 구현

## 프로젝트 구성 및 역할

### 1. 패션 데이터 설계 및 가공
- 텍스트 및 이미지 데이터를 벡터DB 유사도 계산에 최적화되도록 임베딩 수행

### 2. 모델 선정 및 파이프라인 구축
- 사용자 요구에 따른 맞춤형 검색 결과 제공 시스템 개발

### 3. 검색 파이프라인 고도화
- Image Object Detection, Segmentation 등 전처리 단계 구현
- 임베딩 공간에서의 최적화된 검색 결과 제공 파이프라인 구축

## 사용 기술

- **Pinecone**: 벡터DB
- **LlamaIndex**: LLM 응용 프레임워크
- **OpenAI API**: 언어 모델

## 설치 및 실행

### 데이터 다운로드

1. `imaterialist-fashion-2020-fgvc7` 폴더를 생성하고 다음 링크에서 데이터를 다운로드하여 저장하세요:  
   [iMaterialist Fashion 2020 at FGVC7](https://www.kaggle.com/competitions/imaterialist-fashion-2020-fgvc7/data)  

2. `splade` 폴더를 생성하고 다음 GitHub 저장소에서 SPLADE 라이브러리를 다운로드하세요:  
   [SPLADE GitHub Repository](https://github.com/naver/splade)  

### 실행

프로젝트를 실행하려면 다음 명령어를 사용하세요:  
(PineconeDB 설정 및 추가 Database가 필요하므로, 현재 위 코드만으로는 실행되지 않습니다.) 
```bash
streamlit run run.py
```
### 실행 화면
<img src="https://github.com/user-attachments/assets/e485f51b-0042-468b-9abf-511c66e77dcb" width="1000">


----

### 1. Text 상품 검색 (Query : "Vans shoes")
<img src="https://github.com/user-attachments/assets/92f6af0e-e5c6-4608-a60f-e107b5d479b8" width="1000">
<img src="https://github.com/user-attachments/assets/510407bf-2599-4e9b-8251-d0ab6462b64a" width="1000">

----

### 2. Image 상품 검색 (Query : 단일 이미지.jpg)  
<img src="https://github.com/user-attachments/assets/fa33fc9a-d7f3-4bef-91b8-3ff8d7ff795e" width="1000">
<img src="https://github.com/user-attachments/assets/55044585-a428-4bc4-9e8f-a78b66a45ac2" width="1000">

----

### 3. Multi modal 상품 검색 (Query : 이 옷보다 더 차가운 느낌으로 추천해줘, 드레스 이미지.jpg )  
<img src="https://github.com/user-attachments/assets/2e18055a-538c-4630-83a8-7790344814fa" width="1000">
<img src="https://github.com/user-attachments/assets/95a7a9d5-37e9-4826-93de-8f0739183fbd" width="1000">

----

### 4. 생성형AI 기반 패션 생성 (Query : 이 티셔츠를 더 화려하고 빨간색 계열의 옷으로 바꿔줘.)  
<img src="https://github.com/user-attachments/assets/28ede0bc-7f73-4ebc-9760-c2c9ba8009e2" width="1000">
<img src="https://github.com/user-attachments/assets/86868986-4fc5-4f4a-a17c-f3e7b85079fe" width="1000">




