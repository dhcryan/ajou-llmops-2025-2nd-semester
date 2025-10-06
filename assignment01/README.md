# Assignment 01 — Email & Document Writer with Langfuse

## 📌 프로젝트 개요

**주제**: 이메일·문서 자동 작성  
**목적**: Prompt 버전 관리 → 배포 → 추적(Tracing) → 평가(Eval) 전체 사이클 구현

이 프로젝트는 LLM을 활용한 비즈니스 문서 자동 생성 시스템의 프롬프트 엔지니어링 및 버전 관리 프로세스를 시연합니다.

### 🎯 핵심 평가 지표

1. **형식 준수율** (Schema Compliance): 필수 구조 요소 포함 여부
2. **필수 항목 포함률** (Mandatory Items Coverage): must_include 리스트 완성도
3. **톤 일치도** (Tone Consistency): LLM-as-Judge로 0-5점 평가
4. **길이 제한 준수** (Length Control): max_length 이내 작성 여부
5. **편집 필요도** (Edit Need): LLM-as-Judge로 0-5점 평가 (낮을수록 좋음)

---

## 📁 프로젝트 구조

```
assignment01/
├── datasets/
│   └── email_writer_eval.jsonl      # 평가용 데이터셋 (15개 샘플)
├── prompts/
│   ├── email_writer_v1.0.prompty    # V1: 기본 프롬프트
│   └── email_writer_v2.0.prompty    # V2: 개선 프롬프트 (구조화, 제약조건 강화)
├── assignment01_email_writer.ipynb   # 메인 실행 노트북
├── CHANGELOG.md                      # 버전별 변경 이력
├── README.md                         # 이 파일
└── v1_vs_v2_comparison.csv          # 평가 결과 비교표 (실행 후 생성)
```

---

## 🚀 실행 방법

### 1. 환경 설정

```bash
# 가상환경 활성화 (선택사항)
source .venv/bin/activate

# 필요한 패키지 설치
pip install langfuse openai python-dotenv
```

### 2. 환경 변수 설정

프로젝트 루트에 `.env` 파일 생성:

```env
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_HOST=https://cloud.langfuse.com
OPENAI_API_KEY=sk-...
```

### 3. Jupyter Notebook 실행

```bash
jupyter notebook assignment01_email_writer.ipynb
```

또는 VS Code에서 직접 `.ipynb` 파일 열기

### 4. 셀 순차 실행

노트북의 모든 셀을 순서대로 실행하면:
- Langfuse 연결 확인
- Dataset 로드
- Prompt V1, V2 배포
- 각 버전별 5건 이상 실행 (Tracing)
- Dataset을 Langfuse에 업로드
- Evaluation 실행
- V1 vs V2 비교 리포트 생성

---

## 📊 버전 비교 (V1 vs V2)

### V1.0.0 (dev)
- **특징**: 기본적인 이메일 생성
- **입력**: purpose, audience, key_points만 받음
- **한계**: 형식 불일치, 필수 항목 누락 빈번, 톤 불안정

### V2.0.0 (production)
- **특징**: 구조화된 문서 생성, 제약조건 강화
- **입력**: style, tone, must_include, max_length 추가
- **개선**: 
  - 필수 항목 검증 로직 추가
  - 명확한 출력 형식 가이드
  - 전문가 페르소나 설정
  - Critical Rules 5가지 명시

### 기대 성능 개선

| 지표 | V1 (dev) | V2 (production) | 개선도 |
|------|----------|-----------------|--------|
| 필수 항목 포함률 | ~40-60% | ~90-100% | +50%p |
| 길이 제한 준수율 | ~50% | ~95% | +45%p |
| 톤 일치도 (0-5) | ~2.5 | ~4.5 | +2.0 |
| 편집 필요도 (0-5) | ~3.5 | ~1.5 | -2.0 |

---

## 🔗 관련 링크

### Langfuse
- **프로젝트 URL**: `https://cloud.langfuse.com/project/[YOUR_PROJECT_ID]`
- **Prompts**: Langfuse UI > Prompts > `email-writer`
- **Traces**: Langfuse UI > Traces (V1, V2 각 5+ traces)
- **Dataset**: Langfuse UI > Datasets > `email-writer-eval`

### Notion
- **프롬프트 카드 V1**: [Notion 링크 추가 예정]
- **프롬프트 카드 V2**: [Notion 링크 추가 예정]
- **메인 페이지**: [Notion 제출용 허브 링크 추가 예정]

### GitHub
- **Repository**: `https://github.com/dhcryan/ajou-llmops-2025-2nd-semester`
- **과제 폴더**: `/assignment01`

---

## 📝 Notion 프롬프트 카드 필수 필드

각 Notion 프롬프트 카드에는 다음 정보가 포함되어야 합니다:

### Prompt Card Template

| 필드 | 내용 |
|------|------|
| **Project** | Assignment 01 - Email & Document Writer |
| **Prompt Name** | email-writer |
| **Version** | v1.0.0 / v2.0.0 |
| **Goal (지표)** | 형식 준수율, 필수 항목 포함률, 톤 일치도, 편집 필요도 |
| **Change Log** | [CHANGELOG.md 링크] |
| **Dataset Link** | Langfuse Dataset: email-writer-eval |
| **Trace Link** | Langfuse Traces: [링크] |
| **Status** | dev / production |
| **Model** | gpt-4o-mini |
| **Temperature** | 0.7 |

---

## 🧪 평가 방법론

### 정량 평가 (Quantitative)
1. **필수 항목 포함률**: `must_include` 리스트의 각 항목이 출력에 포함되었는지 체크
2. **길이 제한 준수**: 출력 단어 수가 `max_length` 이내인지 확인

### 정성 평가 (Qualitative - LLM-as-Judge)
3. **톤 일치도**: GPT-4o-mini가 지정된 톤과의 일치도를 0-5점 평가
4. **편집 필요도**: GPT-4o-mini가 실무 사용 가능성을 0-5점 평가 (낮을수록 우수)

### 평가 코드 위치
- `assignment01_email_writer.ipynb` 내부의 "Evaluation 함수 정의" 섹션
- 함수: `evaluate_mandatory_items()`, `evaluate_length()`, `llm_judge_tone_consistency()`, `llm_judge_edit_need()`

---

## 📈 주요 발견사항

### V1의 주요 문제점 (Top 3 Failure Cases)
1. **형식 불일치**: 인사말/마무리 누락, 구조 불명확
2. **필수 요소 누락**: `must_include` 항목 50% 미만 포함
3. **톤 불안정**: 문단마다 톤 변화, formal ↔ casual 혼재

### V2의 개선 효과
1. **명확한 구조**: System prompt에 Critical Rules 명시
2. **검증 강화**: 필수 항목 체크리스트 방식으로 강조
3. **페르소나 설정**: "10+ years expert" 역할 부여로 전문성 향상

### 다음 개선안 (V3 고려사항)
1. **Few-shot Examples**: 우수 사례 3-5개 포함하여 형식 학습
2. **JSON Schema 출력**: 구조화된 JSON으로 먼저 출력 후 변환
3. **Chain-of-Thought**: 필수 항목 체크리스트 먼저 작성하게 유도
4. **업종별 세분화**: 이메일/보고서/제안서별 전용 프롬프트
5. **Self-Critique**: 생성 후 자기 검증 단계 추가

---

## 🎓 학습 포인트

이 프로젝트를 통해 다음을 학습합니다:

1. **Prompt Versioning**: 프롬프트를 소프트웨어처럼 버전 관리
2. **Tracing**: Langfuse로 모든 LLM 호출 추적 및 분석
3. **Evaluation Design**: 정량+정성 혼합 평가 설계
4. **LLM-as-Judge**: LLM을 평가자로 활용하는 기법
5. **Iterative Improvement**: 데이터 기반 프롬프트 개선 사이클

---

## 📮 제출 체크리스트

### 파일 준비
- [x] Dataset (15개 샘플 JSONL)
- [x] Prompt V1 (.prompty)
- [x] Prompt V2 (.prompty)
- [x] Jupyter Notebook (실행 가능)
- [x] CHANGELOG.md
- [x] README.md
- [ ] 비교 리포트 CSV (노트북 실행 후 생성)

### Langfuse 설정
- [ ] Prompt V1 배포 (dev 라벨)
- [ ] Prompt V2 배포 (production 라벨)
- [ ] V1 Traces 5건 이상
- [ ] V2 Traces 5건 이상
- [ ] Dataset 업로드 완료
- [ ] smilechacha@ajou.ac.kr 초대 (Viewer 권한)

### Notion 작성
- [ ] 프롬프트 카드 V1 (필수 필드 모두 포함)
- [ ] 프롬프트 카드 V2 (필수 필드 모두 포함)
- [ ] 메인 페이지 (제출용 허브)
- [ ] 체인지로그 링크
- [ ] 실험 리포트

### 최종 제출물
- [ ] Notion 메인 페이지 링크
- [ ] Langfuse 프로젝트 링크
- [ ] GitHub Repository 링크
- [ ] 요약 리포트 PDF (1장)

---

## 👤 작성자

- **이름**: [귀하의 이름]
- **학번**: [귀하의 학번]
- **과목**: LLMOps
- **과제**: Assignment 01
- **제출일**: 2025-10-06

---

## 📄 라이센스

This project is for educational purposes only.
