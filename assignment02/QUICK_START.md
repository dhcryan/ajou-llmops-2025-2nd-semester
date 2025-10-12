# 🚀 Quick Start Guide - Assignment 02

## 빠른 시작 (5분 안에!)

### 1️⃣ 환경 준비

```bash
cd /home/dhc99/ajou-llmops-2025-2nd-semester/assignment02
conda activate torch_env
pip install -q datasets pinecone-client sentence-transformers FlagEmbedding rank-bm25 flashrank python-dotenv pyyaml scikit-learn matplotlib seaborn
```

### 2️⃣ 환경 변수 설정

`.env` 파일을 프로젝트 루트에 생성하고 다음 추가:

```bash
PINECONE_API_KEY=your_api_key_here
```

### 3️⃣ 노트북 실행 순서

**Option A: Jupyter Notebook**
```bash
jupyter notebook
# 브라우저에서 순서대로 실행:
# 1. 01_ingest.ipynb
# 2. 02_index_pinecone.ipynb
# 3. 03_search_eval.ipynb
```

**Option B: VS Code**
```bash
code .
# VS Code에서 노트북 열어서 순서대로 실행
```

---

## 📝 각 노트북 실행 시간

| 노트북 | 예상 시간 | 주요 작업 |
|--------|-----------|-----------|
| 01_ingest.ipynb | ~5분 | 데이터 로드, 청킹, 통계 |
| 02_index_pinecone.ipynb | ~10-15분 | 임베딩 생성, Pinecone 업로드, BM25 인덱싱 |
| 03_search_eval.ipynb | ~15-20분 | 4가지 검색, 평가, 시각화 |

**총 소요 시간: ~30-40분**

---

## 🎯 주요 출력물

실행 후 다음 파일들이 생성됩니다:

```
assignment02/
├── datasets/
│   ├── corpus_chunks.parquet       ← 청킹된 데이터
│   └── eval_queries.jsonl          ← 평가 쿼리
├── artifacts/
│   ├── embeddings.npy              ← 벡터 임베딩
│   ├── bm25_index.pkl              ← BM25 인덱스
│   └── chunks_metadata.parquet     ← 메타데이터
└── results/
    ├── metrics.csv                 ← 평가 결과
    ├── qual_examples.md            ← 사례 분석
    └── plots/
        ├── chunk_statistics.png
        ├── metrics_comparison.png
        └── improvement_over_baseline.png
```

---

## 🔍 예상 결과 미리보기

### 메트릭 비교 (예시)

| Method | Recall@10 | MRR@10 | NDCG@10 |
|--------|-----------|--------|---------|
| Dense | 0.68 | 0.55 | 0.65 |
| BM25 | 0.62 | 0.48 | 0.58 |
| Hybrid (RRF) | 0.76 | 0.63 | 0.72 |
| **Hybrid + Rerank** | **0.85** | **0.72** | **0.80** |

### 개선 효과

- Dense → Hybrid: **+10-15%** 향상
- Hybrid → Hybrid+Rerank: **+8-12%** 추가 향상

---

## ⚡ 트러블슈팅

### ❌ Pinecone API 키 오류

```python
# .env 파일 확인
PINECONE_API_KEY=pcsk_xxxxx...
```

### ❌ CUDA 메모리 부족

```yaml
# configs/models.yaml 수정
embedding:
  device: "cpu"  # cuda → cpu로 변경
```

### ❌ 데이터셋 다운로드 느림

```python
# 01_ingest.ipynb에서 샘플 크기 조정
SAMPLE_SIZE = 200  # 500 → 200으로 감소
```

### ❌ Reranker 모델 로딩 실패

```python
# 대체 모델 사용
reranker:
  model_name: "BAAI/bge-reranker-v2-m3"
```

---

## 📊 다음 단계

노트북 실행 완료 후:

1. **결과 확인**
   ```bash
   cat results/metrics.csv
   ```

2. **그래프 확인**
   ```bash
   ls results/plots/
   ```

3. **Pinecone 초대**
   - https://app.pinecone.io/ 접속
   - 프로젝트 → Settings → Members
   - 강사 이메일 초대

4. **PDF 리포트 작성**
   - `SUBMISSION_GUIDE.md` 참고
   - 5-8페이지 분량
   - 그래프 및 테이블 포함

---

## 🎓 핵심 학습 포인트

이 과제를 통해 배우는 것들:

✅ **검색 기법 비교**
- Dense (의미 검색) vs BM25 (키워드 검색)
- Hybrid 융합 전략 (RRF, Weighted)
- Re-ranking으로 품질 향상

✅ **실무 기술 스택**
- Pinecone (Vector DB)
- BGE-M3 (Multilingual Embeddings)
- Cross-Encoder (Reranking)

✅ **평가 메트릭**
- Recall, MRR, NDCG
- 속도 vs 품질 트레이드오프

✅ **운영 고려사항**
- 배치 처리, 캐싱, 중복 제어
- 메타데이터 활용, 필터링

---

## 💡 Pro Tips

1. **첫 실행 시 작은 샘플로 테스트**
   ```python
   SAMPLE_SIZE = 50  # 빠른 테스트
   ```

2. **GPU 활용** (가능한 경우)
   ```yaml
   embedding:
     device: "cuda"
   ```

3. **Pinecone 인덱스 이름 변경** (중복 방지)
   ```yaml
   pinecone:
     index_name: "rag-assignment-[your-name]"
   ```

4. **결과 저장** 
   - 각 노트북 실행 후 결과 확인
   - 오류 발생 시 로그 저장

---

## 📞 도움이 필요하면?

- **README.md**: 전체 프로젝트 개요
- **SUBMISSION_GUIDE.md**: 제출 체크리스트
- **configs/models.yaml**: 설정 파라미터

**Happy Coding! 🚀**
