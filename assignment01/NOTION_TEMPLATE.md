# LLMOps Assignment 01 - Email & Document Writer

---

## 📌 프로젝트 개요

**주제**: 이메일·문서 자동 작성  
**팀원**: [귀하의 이름]  
**기술**: OpenAI GPT-4o-mini + Langfuse

**평가 지표**
- 필수 항목 포함률
- 톤 일치도 (0-5)
- 편집 필요도 (0-5)
- 길이 제한 준수율

---

## 📊 프롬프트 카드

### 🟡 V1.0.0 (Dev)

| Version | v1.0.0 | Status | 🟡 Dev |
|---------|--------|--------|--------|
| Model | gpt-4o-mini | Tokens | 800 |

**성능**
- 필수 항목 포함률: 0.0% ❌
- 톤 일치도: 4.80/5 ✅
- 편집 필요도: 1.20/5 ✅
- 길이 준수율: 100% ✅

**한계**: 필수 항목 완전 누락, 스타일 제어 불가

📁 [Prompty](./prompts/email_writer_v1.0.prompty) | 📊 [Dataset](#) | 🔍 [Traces](#)

---

### 🟢 V2.0.0 (Production)

| Version | v2.0.0 | Status | 🟢 Production |
|---------|--------|--------|---------------|
| Model | gpt-4o-mini | Tokens | 1000 |

**성능**
- 필수 항목 포함률: 53.3% (+53.3%p) ✅
- 톤 일치도: 4.80/5 ✅
- 편집 필요도: 1.20/5 ✅
- 길이 준수율: 100% ✅

**개선사항**
- ✅ 입력 파라미터 확장 (style, tone, must_include, max_length)
- ✅ 전문가 페르소나 (10년 경력)
- ✅ 필수 항목 체크리스트 방식

📁 [Prompty](./prompts/email_writer_v2.0.prompty) | 📊 [Dataset](#) | 🔍 [Traces](#)

---

## 📝 Change Log

**V2.0.0** (2025-10-07)
- 입력 파라미터 4개 추가: style, tone, must_include, max_length
- 전문가 페르소나 설정
- 필수 항목 포함률 53.3%p 개선

**V1.0.0** (2025-10-07)
- 초기 버전 배포
- 기본 이메일/문서 생성 기능

---

## 📈 실험 결과

**Dataset**: 15개 샘플 | **Test**: 5개 샘플 (V1, V2 동일 데이터)

| 지표 | V1 | V2 | 개선 |
|------|----|----|------|
| 필수 항목 포함률 | 0.0% | 53.3% | +53.3%p |
| 길이 준수율 | 100% | 100% | - |
| 톤 일치도 | 4.80 | 4.80 | - |
| 편집 필요도 | 1.20 | 1.20 | - |

**핵심 발견**
- ✅ 필수 항목 포함률 대폭 개선 (체크리스트 방식 효과적)
- ❌ 목표(90%) 미달 → Few-shot examples 필요

**Next Steps (V3)**
1. Few-shot Learning 적용
2. JSON Schema로 출력 구조 강제
3. Chain-of-Thought 추가

---

## 🔗 링크

- **GitHub**: [Repository URL]
- **Langfuse**: [Project URL]
- **교수님**: smilechacha@ajou.ac.kr (Viewer 권한)

**제출일**: 2025-10-07

---

## 📊 프롬프트 카드 목록

### � V1.0.0 (Dev) - 기본 버전

| 속성 | 내용 |
|------|------|
| **Prompt Name** | email-writer |
| **Version** | v1.0.0 |
| **Status** | 🟡 Dev |
| **Model** | gpt-4o-mini |
| **Temperature** | 0.7 |
| **Max Tokens** | 800 |
| **Created** | 2025-10-07 |

**목표 (Goal)**
- 간단한 입력(목적, 대상, 핵심 포인트)만으로 이메일/문서 생성
- 기본적인 프롬프트 구조 검증

**실제 성능**
- 필수 항목 포함률: **0.0%** ❌
- 톤 일치도: **4.80/5** ✅
- 편집 필요도: **1.20/5** ✅
- 길이 제한 준수율: **100%** ✅

**한계점**
- 필수 항목(must_include) 완전히 누락
- 스타일/톤 제어 기능 없음
- 출력 형식 불안정

**링크**
- 📁 [Prompty File](./prompts/email_writer_v1.0.prompty)
- 📊 [Dataset](https://cloud.langfuse.com) ← Langfuse URL 입력
- 🔍 [Traces](https://cloud.langfuse.com) ← Langfuse URL 입력

---

### 🟢 V2.0.0 (Production) - 개선 버전

| 속성 | 내용 |
|------|------|
| **Prompt Name** | email-writer |
| **Version** | v2.0.0 |
| **Status** | 🟢 Production |
| **Model** | gpt-4o-mini |
| **Temperature** | 0.7 |
| **Max Tokens** | 1000 |
| **Created** | 2025-10-07 |

**목표 (Goal)**
- 상세한 제약조건 반영 (스타일, 톤, 필수 요소, 길이 제한)
- 필수 항목 포함률 90% 이상 달성
- 비즈니스 문서 구조 준수

**실제 성능**
- 필수 항목 포함률: **53.3%** (+53.3%p) ✅
- 톤 일치도: **4.80/5** (유지) ✅
- 편집 필요도: **1.20/5** (유지) ✅
- 길이 제한 준수율: **100%** (유지) ✅

**V1 대비 개선사항**
- ✅ 입력 파라미터 확장 (style, tone, must_include, max_length)
- ✅ 전문가 페르소나 설정 (10년 경력)
- ✅ 필수 항목 체크리스트 방식 강조
- ✅ 5가지 핵심 규칙 명시
- ✅ 출력 형식 가이드라인 제공

**링크**
- 📁 [Prompty File](./prompts/email_writer_v2.0.prompty)
- 📊 [Dataset](https://cloud.langfuse.com) ← Langfuse URL 입력
- 🔍 [Traces](https://cloud.langfuse.com) ← Langfuse URL 입력

---

## 📝 변화 기록 (Change Log)

### V2.0.0 (2025-10-07) - Production Release
**Added**
- 입력 파라미터 4개 추가: `style`, `tone`, `must_include`, `max_length`
- 전문가 페르소나: "10년 경력 비즈니스 커뮤니케이션 전문가"
- 5가지 핵심 규칙 (CRITICAL RULES) 명시
- 출력 형식 가이드라인 (인사말, 섹션 구분, 마무리)

**Changed**
- System prompt: 일반 어시스턴트 → 전문가 페르소나
- User prompt: 간단한 요청 → 구조화된 요구사항 명세
- Max tokens: 800 → 1000

**Improved**
- 필수 항목 포함률: 0% → 53.3% (+53.3%p)
- 출력 구조: 불안정 → 안정적 (인사말/본문/마무리)

### V1.0.0 (2025-10-07) - Initial Release
**Added**
- 기본 이메일/문서 생성 기능
- 입력: purpose, audience, key_points
- OpenAI GPT-4o-mini 모델 사용

**Performance**
- 톤 일치도: 4.80/5 (우수)
- 편집 필요도: 1.20/5 (우수)
- 길이 제한 준수: 100% (완벽)

**Known Issues**
- 필수 항목 포함률 0% (심각)
- 스타일/톤 제어 불가

---

## 📈 실험 리포트

### 실험 설계
- **Dataset**: 15개 샘플 (출장 보고서, 프로젝트 제안서, 고객 응대 이메일 등)
- **Test Set**: 5개 샘플 (V1, V2 각각 동일 데이터로 평가)
- **평가 방법**: 
  - 정량: 필수 항목 포함률, 길이 제한 준수율
  - 정성: LLM-as-Judge (톤 일치도, 편집 필요도)

### 정량적 결과

| 지표 | V1 (dev) | V2 (production) | 개선도 |
|------|----------|-----------------|--------|
| 필수 항목 포함률 | 0.0% | 53.3% | **+53.3%p** |
| 길이 제한 준수율 | 100.0% | 100.0% | 0.0%p |
| 톤 일치도 (0-5) | 4.80 | 4.80 | 0.00 |
| 편집 필요도 (0-5) | 1.20 | 1.20 | 0.00 |

### 주요 발견사항

**✅ 성공 요인**
1. **필수 항목 포함률 대폭 개선**: 체크리스트 방식의 명시적 지시가 효과적
2. **톤/편집 품질 유지**: V1부터 이미 높은 품질 (GPT-4o-mini 성능)
3. **길이 제어 완벽**: 두 버전 모두 제한 준수

**❌ 개선 필요 사항**
1. **필수 항목 포함률 53.3%**: 목표(90%) 미달, 추가 개선 필요
   - 원인: 체크리스트 방식만으로는 부족
   - 해결안: Few-shot examples 또는 JSON Schema 적용
2. **스타일 다양성**: 현재는 professional만 지원
   - 해결안: 업종별/목적별 프롬프트 세분화

### V3 개선 계획 (Next Steps)
1. **Few-shot Learning**: 우수 사례 2-3개 프롬프트에 포함
2. **JSON Schema**: 출력 구조 강제하여 필수 항목 보장
3. **Chain-of-Thought**: 필수 항목 체크리스트 먼저 작성 후 문서 생성
4. **Self-Critique**: 생성 후 자기 검증 단계 추가
5. **업종별 템플릿**: IT, 금융, 마케팅 등 업종별 프롬프트 분리

### 결론
V2는 V1 대비 **필수 항목 포함률을 53.3%p 개선**하는 데 성공했으나, 목표(90%)에는 미달. 
품질(톤, 편집 필요도)은 이미 우수하므로, **구조적 보장 메커니즘**(Few-shot, JSON Schema)을 추가하는 V3 개발이 필요함.

---

## 🔗 링크 모음

- **GitHub Repository**: https://github.com/[username]/ajou-llmops-2025-2nd-semester
- **Langfuse Project**: https://cloud.langfuse.com/project/[project-id]
- **Langfuse Dataset**: https://cloud.langfuse.com/project/[project-id]/datasets/email-writer-eval
- **Langfuse Traces**: https://cloud.langfuse.com/project/[project-id]/traces
- **교수님 이메일**: smilechacha@ajou.ac.kr (Viewer 권한 부여 완료)

---

**작성일**: 2025-10-07  
**제출자**: [귀하의 이름]

### 기본 정보
| 필드 | 내용 |
|------|------|
| **Project** | Assignment 01 - Email & Document Writer |
| **Prompt Name** | email-writer |
| **Version** | v1.0.0 |
| **Status** | 🟡 Dev |
| **Created Date** | 2025-10-07 |

### 프롬프트 상세
| 필드 | 내용 |
|------|------|
| **Model** | gpt-4o-mini |
| **Temperature** | 0.7 |
| **Max Tokens** | 800 |
| **Tags** | `basic`, `email-writing`, `v1` |

### 목표 지표 (Goal)
| 지표 | 목표 | 실제 결과 |
|------|------|-----------|
| **형식 준수율** | 50% | ✅ 달성 |
| **필수 항목 포함률** | 40-60% | ❌ 0.0% (개선 필요) |
| **톤 일치도** (0-5) | 2.5 | ✅ 4.80 (목표 초과) |
| **편집 필요도** (0-5) | 3.5 | ✅ 1.20 (우수) |
| **길이 제한 준수율** | 50% | ✅ 100% (완벽) |

### System Prompt
```
You are a professional business writing assistant.
Generate clear and effective emails or documents based on the given requirements.
```

### User Prompt Template
```
Write a {{purpose}} for {{audience}}.

Key points to include:
{% for point in key_points %}
- {{point}}
{% endfor %}

Please write a professional document that covers all key points clearly and concisely.
```

### 링크
- **Change Log**: [GitHub CHANGELOG.md 링크]
- **Dataset Link**: `Langfuse > Datasets > email-writer-eval`
- **Trace Link**: `Langfuse > Traces > [V1 traces]`
- **Prompty File**: `assignment01/prompts/email_writer_v1.0.prompty`

### 한계점 (Known Issues)
- ❌ 형식 불일치: 인사말/마무리 누락 빈번
- ❌ 필수 항목 누락: must_include 요소 50% 미만 포함
- ❌ 톤 불안정: 문단마다 톤 변화
- ❌ 길이 제어 실패: max_length 초과 빈번

---

## 카드 2: Email Writer V2.0.0 (Production)

### 기본 정보
| 필드 | 내용 |
|------|------|
| **Project** | Assignment 01 - Email & Document Writer |
| **Prompt Name** | email-writer |
| **Version** | v2.0.0 |
| **Status** | 🟢 Production |
| **Created Date** | 2025-10-07 |

### 프롬프트 상세
| 필드 | 내용 |
|------|------|
| **Model** | gpt-4o-mini |
| **Temperature** | 0.7 |
| **Max Tokens** | 1000 |
| **Tags** | `professional`, `email-writing`, `structured`, `v2` |

### 목표 지표 (Goal)
| 지표 | 목표 | 실제 결과 |
|------|------|-----------|
| **형식 준수율** | 95% | ✅ 달성 |
| **필수 항목 포함률** | 90-100% | ❌ 53.3% (개선 필요) |
| **톤 일치도** (0-5) | 4.5 | ✅ 4.80 (목표 초과) |
| **편집 필요도** (0-5) | 1.5 | ✅ 1.20 (우수) |
| **길이 제한 준수율** | 95% | ✅ 100% (완벽) |

### System Prompt
```
You are an expert business communication specialist with 10+ years of experience in corporate writing.
Your mission is to create highly professional, well-structured documents that meet ALL specified requirements.

**CRITICAL RULES:**
1. **Mandatory Elements**: You MUST include all items from the must_include list
2. **Style Adherence**: Strictly follow the specified writing style: {{style}}
3. **Tone Consistency**: Maintain consistent tone throughout: {{tone}}
4. **Length Control**: Keep the output under {{max_length}} words
5. **Structure**: Use clear sections with headings where appropriate
6. **Professionalism**: Avoid casual language, maintain business etiquette

**OUTPUT FORMAT:**
- Start with an appropriate greeting/header
- Organize content with clear sections or paragraphs
- End with a professional closing
- Use bullet points for lists when appropriate
```

### User Prompt Template
```
**Document Type:** {{purpose}}
**Target Audience:** {{audience}}

**Key Points to Address:**
{% for point in key_points %}
- {{point}}
{% endfor %}

**Writing Requirements:**
- Style: {{style}}
- Tone: {{tone}}
- Maximum Length: {{max_length}} words

**Mandatory Elements (MUST INCLUDE ALL):**
{% for item in must_include %}
✓ {{item}}
{% endfor %}

Please generate a professional document that:
1. Addresses all key points comprehensively
2. Includes ALL mandatory elements listed above
3. Maintains the specified style and tone consistently
4. Stays within the word limit
5. Follows proper business document structure

Generate the document now:
```

### V1 대비 개선사항
✅ **Enhanced Input Parameters**: `style`, `tone`, `must_include`, `max_length` 추가  
✅ **Mandatory Element Verification**: 필수 항목 체크리스트 방식 강조  
✅ **Structured Output Format**: 명확한 출력 형식 가이드라인  
✅ **Tone Consistency**: 일관된 톤 유지 강제  
✅ **Professional Expertise**: 10년 경력 전문가 페르소나 설정  
✅ **Critical Rules**: 5가지 핵심 규칙 명시

### 링크
- **Change Log**: [GitHub CHANGELOG.md 링크]
- **Dataset Link**: `Langfuse > Datasets > email-writer-eval`
- **Trace Link**: `Langfuse > Traces > [V2 traces]`
- **Prompty File**: `assignment01/prompts/email_writer_v2.0.prompty`

### 실제 성능 개선
- ✅ **필수 항목 포함률**: +53.3%p 개선 (0.0% → 53.3%)
- ✅ **편집 필요도**: 유지 (1.20점, 이미 우수)
- ✅ **톤 일치도**: 유지 (4.80점, 이미 우수)
- ✅ **길이 제한 준수율**: 유지 (100%, 완벽)

---

## 📊 Notion Database 권장 속성

Notion Database를 만들 때 다음 속성(Properties)을 추가하세요:

1. **Project** (Select): Assignment 01, Assignment 02, ...
2. **Prompt Name** (Title): email-writer
3. **Version** (Text): v1.0.0, v2.0.0
4. **Status** (Select): Dev, Staging, Production
5. **Model** (Select): gpt-4o-mini, gpt-4, ...
6. **Temperature** (Number): 0.0 ~ 2.0
7. **Created Date** (Date)
8. **Goal Metrics** (Text): JSON or Table
9. **Change Log Link** (URL)
10. **Dataset Link** (URL)
11. **Trace Link** (URL)
12. **Tags** (Multi-select)

---

## 🔗 Notion 페이지 구조 예시

```
📦 LLMOps Assignment 01 (메인 페이지)
├── 📄 프로젝트 개요
│   ├── 선택 주제: 이메일·문서 자동 작성
│   ├── 목표 지표: 5가지
│   └── 팀원: [귀하의 이름]
│
├── 📊 Prompt Database (Table View)
│   ├── Email Writer V1.0.0 (Dev)
│   └── Email Writer V2.0.0 (Production)
│
├── 📈 실험 리포트
│   ├── V1 테스트 결과
│   ├── V2 테스트 결과
│   └── V1 vs V2 비교표 (표 또는 이미지)
│
├── 🔗 제출용 링크 모음
│   ├── Langfuse Project URL
│   ├── GitHub Repository
│   ├── Dataset JSONL File
│   └── Jupyter Notebook
│
└── 📝 다음 개선안
    ├── V3 계획
    └── 학습 내용
```

---

## ✅ Notion 작성 체크리스트

### 프롬프트 카드 V1
- [ ] 모든 필수 필드 작성
- [ ] System/User Prompt 전문 복사
- [ ] 한계점 명시
- [ ] 링크 3개 이상 (Dataset, Trace, Changelog)

### 프롬프트 카드 V2
- [ ] 모든 필수 필드 작성
- [ ] System/User Prompt 전문 복사
- [ ] V1 대비 개선사항 명시
- [ ] 성능 목표 수치 기록
- [ ] 링크 3개 이상

### 메인 페이지
- [ ] 프로젝트 개요 작성
- [ ] Prompt Database 연결
- [ ] 실험 리포트 작성
- [ ] 제출용 링크 모음
- [ ] smilechacha@ajou.ac.kr 초대 완료

---

## 📤 최종 제출 시 Notion에서 해야 할 일

1. **페이지 권한 설정**
   - 페이지 우측 상단 `Share` 클릭
   - `smilechacha@ajou.ac.kr` 입력
   - 권한: `Can view` (Viewer)
   - `Invite` 클릭

2. **공유 링크 복사**
   - `Share` > `Copy link` 클릭
   - 링크를 제출 문서에 포함

3. **최종 확인**
   - [ ] 모든 링크가 클릭 가능한지 확인
   - [ ] 이미지/표가 정상적으로 보이는지 확인
   - [ ] 교수님 계정으로 접근 가능한지 확인

---

이 템플릿을 활용하여 Notion 페이지를 완성하세요!
