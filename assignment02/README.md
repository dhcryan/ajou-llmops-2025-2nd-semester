# Assignment 02 - RAG (Retrieval-Augmented Generation)

## 📋 과제 개요

**목표:** Dense, BM25, Hybrid, Hybrid+Re-rank 4가지 검색 방법을 비교하고 RAG 시스템의 검색 품질을 평가합니다.

**데이터셋:** KorQuAD 2.0 (한국어 질의응답 데이터셋)

**핵심 기술 스택:**
- **Vector DB:** Pinecone (Serverless)
- **Embedding:** BGE-M3 (BAAI/bge-m3)
- **BM25:** rank-bm25
- **Reranker:** Jina Reranker v2 Base Multilingual
- **Evaluation:** Recall@5/10, MRR@10, NDCG@10, Latency

---

## 🗂️ 프로젝트 구조

```
assignment02/
├── configs/
│   └── models.yaml              # 모델 및 하이퍼파라미터 설정
├── datasets/
│   ├── corpus_chunks.parquet    # 청킹된 코퍼스 데이터
│   ├── eval_queries.jsonl       # 평가용 쿼리셋
│   └── eval_queries.csv         # 평가용 쿼리 (CSV)
├── artifacts/
│   ├── embeddings.npy           # 임베딩 벡터
│   ├── bm25_index.pkl           # BM25 인덱스
│   └── chunks_metadata.parquet  # 청크 메타데이터
├── results/
│   ├── metrics.csv              # 평가 메트릭 결과
│   ├── qual_examples.md         # 질적 분석 (성공/실패 사례)
│   └── plots/
│       ├── chunk_statistics.png
│       ├── metrics_comparison.png
│       └── improvement_over_baseline.png
├── 01_ingest.ipynb              # 데이터 로드 & 청킹
├── 02_index_pinecone.ipynb      # 임베딩 & 인덱싱
├── 03_search_eval.ipynb         # 검색 & 평가
├── requirements.txt             # 패키지 의존성
└── README.md                    # 본 문서
```

---

## 🚀 실행 방법

### 1. 환경 설정

```bash
# 가상환경 활성화
conda activate torch_env

# 패키지 설치
cd assignment02
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일에 다음 키를 추가하세요:

```bash
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key  # (옵션)
```

### 3. 노트북 실행 순서

```bash
# 1단계: 데이터 준비 및 청킹
jupyter notebook 01_ingest.ipynb

# 2단계: 임베딩 및 Pinecone 인덱싱
jupyter notebook 02_index_pinecone.ipynb

# 3단계: 검색 및 평가
jupyter notebook 03_search_eval.ipynb
```

---

## 🔍 구현 내용

### 1. 데이터 준비 (01_ingest.ipynb)

- **KorQuAD 2.0** 데이터셋 로드 (500 샘플)
- **슬라이딩 윈도우 청킹:**
  - Chunk Size: 512 characters
  - Overlap: 128 characters
- **메타데이터 추가:**
  - `language`: ko
  - `source`: KorQuAD 2.0
  - `doc_id`: 문서 고유 ID
  - `title`: 문서 제목
  - `section`: 청크 섹션 정보
  - `revision_date`: 처리 날짜

### 2. 임베딩 & 인덱싱 (02_index_pinecone.ipynb)

- **임베딩 모델:** BGE-M3 (1024 dim)
- **Pinecone 인덱스:**
  - Metric: Cosine Similarity
  - Serverless (AWS us-east-1)
- **BM25 인덱스:**
  - k1=1.5, b=0.75
  - 토크나이저: 공백 기반

### 3. 검색 & 평가 (03_search_eval.ipynb)

#### 4가지 검색 방법

1. **Dense (Vector Only)**
   - Pinecone 벡터 검색
   - Top-K=10

2. **BM25 (Keyword Only)**
   - rank-bm25 검색
   - Top-K=10

3. **Hybrid (RRF)**
   - Reciprocal Rank Fusion
   - Dense + BM25 결과 융합
   - RRF k=60

4. **Hybrid + Re-rank**
   - Hybrid 검색 (Top-N=100)
   - Cross-Encoder 재순위화
   - Top-K=10

#### 평가 메트릭

- **Recall@5 / Recall@10:** 정답 청크 포함률
- **MRR@10:** 평균 역순위
- **NDCG@10:** 정규화 누적 이득
- **Latency (P50 / P95):** 검색 지연 시간

---

## 📊 예상 결과

| Method | Recall@5 | Recall@10 | MRR@10 | NDCG@10 | Latency (P50) |
|--------|----------|-----------|--------|---------|---------------|
| Dense | 0.65 | 0.72 | 0.58 | 0.68 | 0.15s |
| BM25 | 0.55 | 0.64 | 0.48 | 0.58 | 0.05s |
| Hybrid (RRF) | 0.72 | 0.80 | 0.65 | 0.75 | 0.20s |
| Hybrid + Rerank | **0.80** | **0.88** | **0.73** | **0.82** | 0.50s |

*실제 결과는 데이터셋과 설정에 따라 다를 수 있습니다.*

---

## 📈 주요 인사이트

### 1. 검색 품질 개선
- **Hybrid 방법**이 Dense나 BM25 단독 사용 대비 **10-15% 성능 향상**
- **Re-ranking**으로 추가 **8-12% 개선** 가능

### 2. 속도 vs 품질 트레이드오프
- **BM25:** 가장 빠르지만 의미 검색 약점
- **Dense:** 빠르고 의미 검색 강점
- **Hybrid + Rerank:** 최고 품질이지만 가장 느림 (3-4배)

### 3. 실무 적용 전략
- **실시간 서비스:** Dense or Hybrid (RRF)
- **배치 처리:** Hybrid + Rerank
- **하이브리드 α 튜닝:** 도메인 특성에 따라 조정

---

## ✅ 체크리스트

### 필수 제출물

- [x] **노트북 3개**
  - [x] 01_ingest.ipynb
  - [x] 02_index_pinecone.ipynb
  - [x] 03_search_eval.ipynb

- [ ] **데이터/설정**
  - [ ] corpus_chunks.parquet
  - [ ] configs/models.yaml
  - [ ] eval_queries.jsonl

- [ ] **결과물**
  - [ ] results/metrics.csv
  - [ ] results/plots/ (3개 그래프)
  - [ ] results/qual_examples.md

- [ ] **Pinecone 공유**
  - [ ] 프로젝트에 강사 초대
  - [ ] 초대 스크린샷 캡처

- [ ] **리포트 (PDF, 5-8페이지)**
  - [ ] 데이터셋 및 청킹 전략
  - [ ] 모델 선택 근거
  - [ ] 하이브리드 설계 (RRF/α 파라미터)
  - [ ] 재순위화 전략 (N/k)
  - [ ] 메트릭 분석 및 그래프
  - [ ] 오류 분석 및 개선안

---

## 🔧 설정 파일 (models.yaml)

주요 하이퍼파라미터:

```yaml
# Embedding
embedding:
  model_name: "BAAI/bge-m3"
  dimension: 1024
  normalize: true

# Hybrid
hybrid:
  method: "rrf"          # "rrf" or "weighted"
  rrf_k: 60              # RRF 상수
  alpha: 0.5             # Dense 가중치 (weighted 방식)

# Reranker
reranker:
  model_name: "jinaai/jina-reranker-v2-base-multilingual"
  top_n: 100             # 재순위화 전 후보
  top_k: 10              # 최종 결과 수

# Retrieval
retrieval:
  top_k: 10
  deduplicate: true
  max_chunks_per_doc: 3  # 문서당 최대 청크 수
```

---

## 📚 참고 자료

- [Pinecone Documentation](https://docs.pinecone.io/)
- [BGE-M3 Model Card](https://huggingface.co/BAAI/bge-m3)
- [Jina Reranker](https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual)
- [KorQuAD 2.0 Paper](https://arxiv.org/abs/1909.07005)
- [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)

