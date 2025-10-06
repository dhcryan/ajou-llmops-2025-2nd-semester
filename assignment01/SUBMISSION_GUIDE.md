# 과제 01 제출 가이드

## 📋 제출 전 최종 체크리스트

### 1️⃣ 코드 및 파일 준비 ✅

#### assignment01 폴더 구조 확인
```bash
cd /home/dhc99/ajou-llmops-2025-2nd-semester/assignment01
tree
```

필수 파일:
- [x] `datasets/email_writer_eval.jsonl` (15개 샘플)
- [x] `prompts/email_writer_v1.0.prompty`
- [x] `prompts/email_writer_v2.0.prompty`
- [x] `assignment01_email_writer.ipynb`
- [x] `CHANGELOG.md`
- [x] `README.md`
- [x] `NOTION_TEMPLATE.md`
- [ ] `v1_vs_v2_comparison.csv` (노트북 실행 후 생성됨)

---

### 2️⃣ Jupyter Notebook 실행 🚀

#### 단계별 실행
1. `.env` 파일에 API 키가 설정되어 있는지 확인
2. `assignment01_email_writer.ipynb` 열기
3. 모든 셀을 순차적으로 실행 (Shift + Enter)
4. 각 단계별 출력 확인:
   - ✅ 환경 변수 로드 성공
   - ✅ Langfuse 연결 성공
   - ✅ Dataset 로드 (15개)
   - ✅ Prompt V1, V2 배포 완료
   - ✅ V1 테스트 5건 실행 + Trace
   - ✅ V2 테스트 5건 실행 + Trace
   - ✅ Dataset 업로드 완료
   - ✅ Evaluation 실행
   - ✅ 비교표 생성 (`v1_vs_v2_comparison.csv`)

#### 예상 실행 시간
- 전체 셀 실행: 약 5-10분
- Trace 생성: V1 5건 + V2 5건 = 총 10건 이상
- LLM-as-Judge 평가: 추가 10건 이상

---

### 3️⃣ Langfuse 설정 🔗

#### Langfuse UI에서 확인할 사항

1. **Prompts 페이지**
   - `email-writer` 프롬프트 존재
   - V1 버전: `dev` 라벨
   - V2 버전: `production` 라벨
   - 각 버전의 내용이 .prompty 파일과 일치

2. **Traces 페이지**
   - 총 10건 이상의 Trace 존재
   - V1 traces: 5건 이상 (name: `v1-test-e001`, `v1-test-e002`, ...)
   - V2 traces: 5건 이상 (name: `v2-test-e001`, `v2-test-e002`, ...)
   - 각 Trace의 metadata 확인 (purpose, audience, version 등)

3. **Datasets 페이지**
   - Dataset 이름: `email-writer-eval`
   - 아이템 수: 15개
   - 각 아이템에 input, expected_output 존재

4. **사용자 초대**
   - Settings > Members > Invite
   - 이메일: `smilechacha@ajou.ac.kr`
   - 역할: `Viewer` 이상
   - ✅ 초대 완료 확인

#### Langfuse 프로젝트 URL 복사
```
https://cloud.langfuse.com/project/[YOUR_PROJECT_ID]
```
이 URL을 Notion 및 제출 문서에 포함하세요.

---

### 4️⃣ Notion 페이지 작성 📝

#### Notion Database 생성
1. Notion에서 새 페이지 생성: "LLMOps Assignment 01"
2. Database (Table) 추가
3. 속성(Properties) 설정 (NOTION_TEMPLATE.md 참고)

#### 프롬프트 카드 2개 작성
- **카드 1**: Email Writer V1.0.0 (Dev)
  - 모든 필수 필드 작성
  - System/User Prompt 전문 복사
  - 한계점 명시
  
- **카드 2**: Email Writer V2.0.0 (Production)
  - 모든 필수 필드 작성
  - V1 대비 개선사항 명시
  - 성능 목표 기록

#### 필수 섹션 작성
1. **프로젝트 개요**
   - 선택 주제: 이메일·문서 자동 작성
   - 목표 지표: 5가지
   - 작성자 정보

2. **실험 리포트**
   - V1 vs V2 비교표 (표 또는 이미지)
   - 주요 발견사항
   - 실패 사례 Top-3

3. **제출용 링크 모음**
   - Langfuse Project URL
   - GitHub Repository
   - Dataset JSONL
   - Jupyter Notebook

#### Notion 공유 설정
1. 우측 상단 `Share` 클릭
2. `smilechacha@ajou.ac.kr` 초대 (Can view)
3. 공유 링크 복사

---

### 5️⃣ GitHub 확인 💻

#### Repository 상태 확인
```bash
cd /home/dhc99/ajou-llmops-2025-2nd-semester
git status
```

#### Commit 및 Push
```bash
# 변경사항 확인
git add assignment01/

# Commit
git commit -m "Complete Assignment 01: Email & Document Writer with Langfuse"

# Push
git push origin main
```

#### GitHub에서 확인할 사항
- [ ] `assignment01/` 폴더 전체가 업로드되었는지 확인
- [ ] `README.md`가 제대로 렌더링되는지 확인
- [ ] `.env` 파일은 **절대** 업로드하지 않았는지 확인 (gitignore 확인)

---

### 6️⃣ 요약 리포트 PDF 작성 📄

#### 리포트 구성 (1페이지)
아래 내용을 PDF로 작성하세요 (A4 1장):

```
========================================
LLMOps Assignment 01 요약 리포트
========================================

1. 프로젝트 개요
- 주제: 이메일·문서 자동 작성
- 평가 지표: 형식 준수율, 필수 항목 포함률, 톤 일치도, 편집 필요도, 길이 제한 준수

2. V1 vs V2 성능 비교표
┌─────────────────────┬──────────┬──────────┬──────────┐
│ 지표                │ V1 (dev) │ V2 (prod)│ 개선도   │
├─────────────────────┼──────────┼──────────┼──────────┤
│ 필수 항목 포함률    │ XX.X%    │ XX.X%    │ +XX.Xp   │
│ 길이 제한 준수율    │ XX.X%    │ XX.X%    │ +XX.Xp   │
│ 톤 일치도 (0-5)     │ X.XX     │ X.XX     │ +X.XX    │
│ 편집 필요도 (0-5)   │ X.XX     │ X.XX     │ -X.XX    │
└─────────────────────┴──────────┴──────────┴──────────┘

3. 핵심 개선사항 (V1 → V2)
① Enhanced Input Parameters: style, tone, must_include, max_length 추가
② Mandatory Element Verification: 필수 항목 체크리스트 방식 강제
③ Professional Expertise: 10년 경력 전문가 페르소나 설정
④ Critical Rules: 5가지 핵심 규칙 명시
⑤ Structured Output Format: 명확한 출력 형식 가이드라인

4. 주요 실패 사례 (V1 기준 Top-3)
① 사례 e001: 편집 필요도 4/5 - 필수 항목 누락, 구조화 부족
② 사례 e003: 편집 필요도 4/5 - 톤 불일치, 형식 불명확
③ 사례 e004: 편집 필요도 3/5 - 길이 초과, 핵심 누락

5. 다음 개선안 (V3 고려사항)
① Few-shot Examples 추가 → 형식 일관성 향상
② JSON Schema 출력 → 구조화 강제
③ Chain-of-Thought → 체크리스트 먼저 작성
④ 업종별 세분화 → 이메일/보고서/제안서 전용 프롬프트
⑤ Self-Critique 추가 → 생성 후 자기 검증

6. 제출 링크
- Notion: [URL]
- Langfuse: [URL]
- GitHub: [URL]

작성자: [이름] ([학번])
제출일: 2025-10-06
========================================
```

#### PDF 생성 방법
- **Option 1**: Google Docs로 작성 후 PDF 다운로드
- **Option 2**: Notion 페이지를 PDF로 Export
- **Option 3**: Markdown을 pandoc으로 PDF 변환

---

### 7️⃣ 최종 제출 📤

#### 제출 항목 정리

1. **Notion 메인 페이지 링크**
   ```
   https://www.notion.so/[your-page-id]
   ```

2. **Langfuse 프로젝트 링크**
   ```
   https://cloud.langfuse.com/project/[YOUR_PROJECT_ID]
   ```

3. **GitHub Repository 링크**
   ```
   https://github.com/dhcryan/ajou-llmops-2025-2nd-semester
   ```

4. **요약 리포트 PDF**
   - 파일명: `assignment01_summary_report_[학번].pdf`

#### 제출 방법
과제 제출 시스템에 다음 내용을 포함한 텍스트 문서 제출:

```
========================================
LLMOps Assignment 01 제출
========================================

이름: [귀하의 이름]
학번: [귀하의 학번]
제출일: 2025-10-06

1. Notion 메인 페이지
   URL: [Notion 링크]
   권한: smilechacha@ajou.ac.kr 초대 완료 (Viewer)

2. Langfuse 프로젝트
   URL: [Langfuse 링크]
   권한: smilechacha@ajou.ac.kr 초대 완료 (Viewer)
   - Prompts: email-writer (V1 dev, V2 production)
   - Traces: 10+ traces (V1: 5+, V2: 5+)
   - Dataset: email-writer-eval (15 items)

3. GitHub Repository
   URL: https://github.com/dhcryan/ajou-llmops-2025-2nd-semester
   폴더: /assignment01
   - README.md: 프로젝트 개요 및 실행 방법
   - Dataset: datasets/email_writer_eval.jsonl
   - Prompts: prompts/email_writer_v1.0.prompty, v2.0.prompty
   - Notebook: assignment01_email_writer.ipynb
   - CHANGELOG: CHANGELOG.md

4. 요약 리포트
   첨부 파일: assignment01_summary_report_[학번].pdf

5. 주요 성과
   - V1 → V2 필수 항목 포함률 +XX.X%p 개선
   - 편집 필요도 -X.X점 개선
   - Langfuse 전체 사이클 구현 완료

========================================
```

---

## ⚠️ 주의사항

### 금지 사항
- ❌ `.env` 파일을 GitHub에 업로드하지 마세요
- ❌ API 키를 노트북에 하드코딩하지 마세요
- ❌ 개인정보가 포함된 데이터 사용 금지
- ❌ 제출 전 교수님 초대를 잊지 마세요

### 권장 사항
- ✅ 노트북 실행 전 `.env` 파일 확인
- ✅ Langfuse에서 Trace가 제대로 남았는지 확인
- ✅ Notion 페이지가 공개 상태인지 확인
- ✅ 모든 링크가 클릭 가능한지 테스트

---

## 🆘 문제 해결

### Langfuse 연결 실패
```python
# .env 파일 확인
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_HOST=https://cloud.langfuse.com
```

### OpenAI API 오류
```python
# API 키 확인
OPENAI_API_KEY=sk-...
# Rate limit 오류 시 time.sleep() 추가
```

### Notion 초대 실패
- Notion 페이지 설정 > Share
- 이메일 주소 정확히 입력: `smilechacha@ajou.ac.kr`
- Can view 권한 선택

---

## ✅ 최종 체크리스트

### 코드 & 파일
- [ ] Dataset 15개 샘플 준비
- [ ] Prompt V1, V2 작성
- [ ] Jupyter Notebook 전체 실행 완료
- [ ] v1_vs_v2_comparison.csv 생성됨
- [ ] README.md 작성

### Langfuse
- [ ] Prompt V1 배포 (dev 라벨)
- [ ] Prompt V2 배포 (production 라벨)
- [ ] Traces 10건 이상 생성
- [ ] Dataset 업로드 완료
- [ ] smilechacha@ajou.ac.kr 초대 (Viewer)

### Notion
- [ ] 프롬프트 카드 2개 작성
- [ ] 모든 필수 필드 포함
- [ ] 실험 리포트 작성
- [ ] 제출용 링크 모음
- [ ] smilechacha@ajou.ac.kr 초대 (Can view)

### GitHub
- [ ] assignment01 폴더 push 완료
- [ ] README.md 정상 렌더링
- [ ] .env 파일 제외됨

### 제출
- [ ] 요약 리포트 PDF 작성
- [ ] 제출 텍스트 문서 준비
- [ ] 모든 링크 테스트 완료
- [ ] 제출 완료!

---

**제출 기한을 꼭 확인하세요!** 🚀

Good luck! 🎉
