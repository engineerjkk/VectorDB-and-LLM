# 벡터DB와 LLM 기반 상품 검색 및 추천 시스템

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

```bash
streamlit run run.py
```
### 실행 화면
1. Text 상품 검색 (Query : "Vans shoes")  
![image](https://github.com/user-attachments/assets/8e332449-9f93-46c4-8e59-e8373d511f22)  
2. Image 상품 검색 (Query : 단일 이미지.jpg)  
![image](https://github.com/user-attachments/assets/e0c90470-f30c-4c5f-b917-02928171ce15)  
3. Multi modal 상품 검색 (Query : 이 따뜻한 느낌으로 어울릴 만한 상품을 추천해줘, 코트 이미지.jpg )  
![image](https://github.com/user-attachments/assets/90f55eb9-db78-4e36-b9c4-b5b666aa649b)
4. Stable Diffusion 패션 생성 (Query : 이 드레스를 빨간색으로 바꿔줘)  
![image](https://github.com/user-attachments/assets/ca083cfc-89f9-4c84-a2ba-09d759727d68)  

