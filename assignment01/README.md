# Assignment 01 — Email Writer with Langfuse

## 📌 개요
**주제**: 이메일·문서 자동 작성  
**목적**: Prompt 버전 관리 → Tracing → Evaluation 사이클 구현

## 📁 구조
```
assignment01/
├── datasets/email_writer_eval.jsonl       # 평가 데이터셋 (15개 샘플)
├── prompts/
│   ├── email_writer_v1.0.prompty         # V1: 기본 프롬프트
│   └── email_writer_v2.0.prompty         # V2: 개선 프롬프트
├── assignment01_email_writer.ipynb        # 메인 실행 노트북
├── v1_vs_v2_comparison.csv               # 평가 결과
└── CHANGELOG.md                           # 변경 이력
```

## 🚀 실행 방법

### 1. 환경 설정
```bash
pip install langfuse openai python-dotenv
```

### 2. `.env` 파일 생성
```env
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_HOST=https://cloud.langfuse.com
OPENAI_API_KEY=sk-...
```

### 3. 노트북 실행
`assignment01_email_writer.ipynb` 파일의 모든 셀을 순차 실행

## 📊 버전 비교

### V1.0 (dev) → V2.0 (production)

**V1 한계점**:
- purpose, audience, key_points만 입력
- 형식 불일치, 필수 항목 누락 빈번

**V2 개선사항**:
- style, tone, must_include, max_length 파라미터 추가
- Critical Rules 명시, 전문가 페르소나 설정

**실행 결과** (2025-10-07):

| 지표 | V1 | V2 | 개선도 |
|------|----|----|--------|
| 필수 항목 포함률 | 0.0% | 53.3% | +53.3%p |
| 톤 일치도 (0-5) | 4.80 | 4.80 | - |
| 편집 필요도 (0-5) | 1.20 | 1.20 | - |
| 길이 제한 준수 | 100% | 100% | - |

## 🧪 평가 방법

**정량 평가**:
- 필수 항목 포함률: `must_include` 리스트 체크
- 길이 제한: `max_length` 이내 여부

**정성 평가 (LLM-as-Judge)**:
- 톤 일치도: 0-5점 (높을수록 좋음)
- 편집 필요도: 0-5점 (낮을수록 좋음)


