# Assignment 02 - 제출 체크리스트

## 📋 최종 제출 체크리스트

### ✅ 1. 코드 및 노트북 (30점)

- [ ] **01_ingest.ipynb** - 데이터 로드 및 청킹
  - [ ] KorQuAD 2.0 로드 완료
  - [ ] 슬라이딩 윈도우 청킹 구현
  - [ ] 메타데이터 필드 추가 (language, source, doc_id, title, section, revision_date)
  - [ ] 청크 통계 및 시각화
  - [ ] 평가용 쿼리셋 생성
  - [ ] corpus_chunks.parquet 저장

- [ ] **02_index_pinecone.ipynb** - 임베딩 및 인덱싱
  - [ ] BGE-M3 모델 로드
  - [ ] Pinecone 인덱스 생성 (cosine metric)
  - [ ] 청크 임베딩 생성
  - [ ] Pinecone에 벡터 업로드 (batch upsert)
  - [ ] BM25 인덱스 생성 및 저장
  - [ ] 검색 테스트 (Dense & BM25)

- [ ] **03_search_eval.ipynb** - 검색 및 평가
  - [ ] Dense 검색 구현
  - [ ] BM25 검색 구현
  - [ ] Hybrid 검색 구현 (RRF 또는 Weighted)
  - [ ] Hybrid + Re-rank 구현 (Cross-Encoder)
  - [ ] 평가 메트릭 함수 (Recall@5/10, MRR@10, NDCG@10)
  - [ ] 전체 평가 실행
  - [ ] 결과 시각화 (비교 그래프)
  - [ ] 질적 분석 (성공/실패 사례)

### ✅ 2. 데이터 및 설정 파일 (10점)

- [ ] **configs/models.yaml**
  - [ ] 임베딩 모델 설정
  - [ ] Pinecone 설정
  - [ ] BM25 파라미터
  - [ ] Hybrid 방법 및 파라미터 (RRF k 또는 α)
  - [ ] Reranker 설정 (top_n, top_k)
  - [ ] 청킹 설정
  - [ ] 평가 설정

- [ ] **datasets/**
  - [ ] corpus_chunks.parquet (500-2000 청크)
  - [ ] eval_queries.jsonl (20-50 쿼리)
  - [ ] eval_queries.csv

- [ ] **artifacts/**
  - [ ] embeddings.npy
  - [ ] bm25_index.pkl
  - [ ] chunks_metadata.parquet

### ✅ 3. 결과물 (25점)

- [ ] **results/metrics.csv**
  - [ ] 4개 방법 (Dense, BM25, Hybrid, Hybrid+Rerank)
  - [ ] 모든 메트릭 포함 (Recall@5/10, MRR@10, NDCG@10, Latency)
  - [ ] 평균값 및 백분위수

- [ ] **results/plots/**
  - [ ] chunk_statistics.png - 청크 통계
  - [ ] metrics_comparison.png - 메트릭 비교
  - [ ] improvement_over_baseline.png - 개선 폭

- [ ] **results/qual_examples.md**
  - [ ] 최소 5개 사례 분석
  - [ ] 성공/실패 원인 분석
  - [ ] 개선 포인트 제시

### ✅ 4. Pinecone 공유 (15점)

- [ ] **Pinecone 프로젝트 초대**
  - [ ] 강사 이메일로 멤버 초대
  - [ ] 권한: Viewer 또는 Editor
  - [ ] 초대 완료 스크린샷 캡처
  - [ ] 스크린샷에 프로젝트명, 강사 이메일, 권한 표시

### ✅ 5. 리포트 (PDF, 5-8페이지) (20점)

#### 섹션별 체크리스트:

**1. 서론 (1페이지)**
- [ ] 과제 목표 및 배경
- [ ] 사용 기술 스택 개요
- [ ] 데이터셋 소개

**2. 데이터 준비 (1-1.5페이지)**
- [ ] KorQuAD 2.0 선택 근거
- [ ] 청킹 전략 설명 (슬라이딩 윈도우, 크기, 오버랩)
- [ ] 메타데이터 필드 및 목적
- [ ] 청크 통계 (개수, 길이 분포)
- [ ] 표/그래프 포함

**3. 모델 및 설계 (1.5-2페이지)**
- [ ] **임베딩 모델:** BGE-M3 선택 근거
- [ ] **Pinecone 설정:** Metric, dimension, serverless 선택 이유
- [ ] **BM25 파라미터:** k1=1.5, b=0.75 근거
- [ ] **Hybrid 설계:**
  - [ ] RRF vs Weighted 선택 근거
  - [ ] RRF k=60 또는 α=0.5 설정 근거
- [ ] **Reranker 설계:**
  - [ ] Jina Reranker 선택 이유
  - [ ] Top-N=100, Top-K=10 설정 근거
  - [ ] 중복 제어 전략 (max_chunks_per_doc)

**4. 평가 결과 (2-2.5페이지)**
- [ ] **메트릭 테이블:** 4개 방법 비교
- [ ] **그래프:**
  - [ ] Recall@5 vs Recall@10
  - [ ] MRR@10, NDCG@10
  - [ ] Latency P50/P95
  - [ ] Baseline 대비 개선 폭
- [ ] **수치 분석:**
  - [ ] Dense → Hybrid 개선 효과
  - [ ] Hybrid → Hybrid+Rerank 개선 효과
  - [ ] 속도 vs 품질 트레이드오프

**5. 질적 분석 (1-1.5페이지)**
- [ ] **성공 사례 (2-3개)**
  - [ ] Hybrid+Rerank가 Dense보다 우수한 사례
  - [ ] 원인 분석 (키워드 매칭, 의미 이해 등)
- [ ] **실패 사례 (2-3개)**
  - [ ] 모든 방법이 실패한 쿼리
  - [ ] 원인 분석:
    - [ ] 청킹 문제 (답변이 여러 청크에 분산)
    - [ ] 약어/전문용어 불일치
    - [ ] 표/리스트 구조 손실
    - [ ] 버전/시점 차이

**6. 개선안 (1페이지)**
- [ ] **검색 품질 개선:**
  - [ ] 필드별 가중치 (title > text)
  - [ ] 메타데이터 필터링 (날짜, 출처)
  - [ ] 중복 제어 강화
- [ ] **운영 최적화:**
  - [ ] 캐싱 전략
  - [ ] 배치 처리
  - [ ] 폴백 전략 (검색 실패 시)
- [ ] **청킹 개선:**
  - [ ] 의미 기반 청킹 (Semantic Chunking)
  - [ ] 문맥 보존 (앞뒤 문장 포함)
  - [ ] 표/리스트 특수 처리

**7. 결론 (0.5페이지)**
- [ ] 핵심 인사이트 요약
- [ ] Hybrid+Rerank의 실무 적용 가능성
- [ ] 향후 연구 방향

### ✅ 6. 추가 사항

- [ ] **README.md**
  - [ ] 프로젝트 구조 설명
  - [ ] 실행 방법
  - [ ] 트러블슈팅 가이드

- [ ] **requirements.txt**
  - [ ] 모든 패키지 버전 명시

- [ ] **Git Repository**
  - [ ] 코드 커밋
  - [ ] 적절한 커밋 메시지
  - [ ] .gitignore 설정 (artifacts 제외 고려)

---

## 📊 평가 기준 (100점)

| 항목 | 배점 | 평가 요소 |
|------|------|-----------|
| **검색 품질** | 35점 | - Dense → BM25 → Hybrid → Hybrid+Rerank 개선 폭<br>- Recall, NDCG, MRR 향상<br>- 정답 포함률 증가 |
| **설계 타당성** | 25점 | - α/RRF 파라미터 근거<br>- N/k 설정 합리성<br>- 중복 제어 전략<br>- 청킹/메타/필터 설계 |
| **운영성** | 15점 | - Pinecone 공유/권한 확인<br>- 인덱스 성능 인사이트<br>- 캐시/지연 최적화<br>- 폴백 전략 고려 |
| **근거성** | 15점 | - 스니펫 하이라이트 제공<br>- 출처/개정일 일관 표시<br>- 검색 결과 투명성 |
| **리포트 완성도** | 10점 | - 명료한 구조<br>- 그래프/표 품질<br>- 실패 원인 분석 구체성<br>- 개선안 실용성 |

---

## 📅 제출 마감

- **마감일:** [강사 공지 참조]
- **제출 방법:** [강사 공지 참조]
- **제출 형식:**
  - Git Repository URL 또는
  - ZIP 파일 (assignment02_[학번]_[이름].zip)

---

## 🚨 주의사항

1. **Pinecone 초대 필수**
   - 프로젝트 멤버 초대 없이 제출 시 감점
   - 스크린샷 필수 포함

2. **데이터 저작권**
   - KorQuAD 2.0은 오픈소스이나, 재배포 시 출처 명시
   - 상업적 이용 금지

3. **코드 실행 가능성**
   - 제출 전 전체 노트북 재실행 확인
   - 경로 하드코딩 지양 (상대 경로 사용)

4. **표절 금지**
   - 팀원 간 코드 공유 금지
   - 참고 자료 명시

---

## ✅ 최종 확인

제출 전 아래 항목을 모두 확인하세요:

- [ ] 모든 노트북이 에러 없이 실행됨
- [ ] metrics.csv에 4개 방법 결과 포함
- [ ] 그래프 3개 생성됨
- [ ] qual_examples.md에 5개 이상 사례 포함
- [ ] Pinecone 초대 완료 및 스크린샷 캡처
- [ ] PDF 리포트 5-8페이지 작성
- [ ] README.md 작성 완료
- [ ] Git에 커밋 및 푸시 (또는 ZIP 압축)

---

**Good Luck! 🎉**
