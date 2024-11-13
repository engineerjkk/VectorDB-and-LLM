# 벡터DB와 LLM 기반 상품 검색 및 추천 시스템 🔍

## 📌 서비스 링크
> [🌐 웹 페이지 바로가기](http://34.47.106.54:8501/)   
> ※ 과금 이슈로 임시 중단 중 (문의: engineerjkk@naver.com)

## 💡 프로젝트 개요
- **기간**: 4개월 (2024.05 ~ 2024.08)
- **유형**: 개인 프로젝트
- **목적**: Deep Metric Learning 및 이미지 검색 연구 경험을 활용한 LLM 기반 상품 추천 시스템 개발

## 🔧 핵심 기능
1. **멀티모달 쿼리 처리**
   - 텍스트/이미지 기반 검색
   - 고차원 벡터 임베딩 생성

2. **개인화 추천**
   - 벡터 유사도 기반 검색
   - 맞춤형 상품 추천

3. **AI 기반 패션 생성**
   - 사용자 요구사항 기반 패션 아이템 생성
   - 스타일 변환 및 추천

## 🛠 기술 스택
- **벡터 데이터베이스**: Pinecone
- **LLM 프레임워크**: LlamaIndex
- **AI 모델**: OpenAI API
- **이미지 처리**: Object Detection, Segmentation

## 📂 시스템 구성

### 1. 데이터 파이프라인
- 텍스트/이미지 데이터 전처리
- 벡터 임베딩 최적화
- 유사도 계산 알고리즘 구현

### 2. 검색 시스템
- 멀티모달 쿼리 처리
- 실시간 검색 결과 제공
- 개인화 추천 알고리즘

## 🚀 설치 및 실행

### 데이터 준비

#### 1. iMaterialist Fashion 데이터셋 설치
1. `imaterialist-fashion-2020-fgvc7` 폴더 생성
2. [iMaterialist Fashion 2020 at FGVC7](https://www.kaggle.com/competitions/imaterialist-fashion-2020-fgvc7/data) 에서 데이터 다운로드
3. 다운로드한 데이터를 생성한 폴더에 저장

#### 2. SPLADE 라이브러리 설치
1. `splade` 폴더 생성
2. [SPLADE GitHub Repository](https://github.com/naver/splade) 에서 라이브러리 다운로드
3. 다운로드한 파일을 생성한 폴더에 저장

### 실행 방법
```bash
streamlit run run.py
```
※ PineconeDB 설정 및 추가 데이터베이스 필요

## 📱 서비스 데모

### 1. 텍스트 기반 검색 (Query: "Vans shoes")
<p align="center">
  <img src="https://github.com/user-attachments/assets/92f6af0e-e5c6-4608-a60f-e107b5d479b8" width="1000">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/510407bf-2599-4e9b-8251-d0ab6462b64a" width="1000">
</p>

### 2. 이미지 기반 검색
<p align="center">
  <img src="https://github.com/user-attachments/assets/fa33fc9a-d7f3-4bef-91b8-3ff8d7ff795e" width="1000">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/55044585-a428-4bc4-9e8f-a78b66a45ac2" width="1000">
</p>

### 3. 멀티모달 검색 (Query: 이 옷보다 더 차가운 느낌으로 추천해줘)
<p align="center">
  <img src="https://github.com/user-attachments/assets/2e18055a-538c-4630-83a8-7790344814fa" width="1000">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/95a7a9d5-37e9-4826-93de-8f0739183fbd" width="1000">
</p>

### 4. AI 패션 생성 (Query: 이 티셔츠를 더 화려하고 빨간색 계열의 옷으로 바꿔줘)
<p align="center">
  <img src="https://github.com/user-attachments/assets/28ede0bc-7f73-4ebc-9760-c2c9ba8009e2" width="1000">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/86868986-4fc5-4f4a-a17c-f3e7b85079fe" width="1000">
</p>
