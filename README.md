# AI융합실전프로젝트10 - LLMOps 강의계획서
**아주대학교 AI대학원 2025년 2학기**

## 📅 주차별 강의 계획

- **Week 1**: LLM 라이프사이클 OT & 환경 세팅
- **Week 2**: PromptOps 기초
- **Week 3**: 프롬프트 평가 및 버저닝
- **Week 4**: RAG 기본 및 벡터DB
- **Week 5**: 고급 RAG (Hybrid Search & 재순위화)
- **Week 6**: 파인튜닝 I (SFT, LoRA)
- **Week 7**: 파인튜닝 II (DPO)
- **Week 8**: 중간고사
- **Week 9**: 추론 최적화 & FastAPI
- **Week 10**: LLMOps 스택
- **Week 11**: 합성 데이터 & RAG 평가
- **Week 12**: 에이전트 체이닝
- **Week 13**: 보안 & 안전성
- **Week 14**: 비용 최적화 & 오토스케일링
- **Week 15**: Capstone 설계 워크숍
- **Week 16**: 기말고사

---

## ⚙️ 환경 설정 안내
- 수업 코드 실행 전, 프로젝트 루트에서 아래 명령을 실행하세요:
  ```bash
  cp .env.sample .env

* 생성된 `.env` 파일 안에 개인의 `OPENAI_API_KEY`를 직접 입력합니다:

  ```env
  OPENAI_API_KEY=your_secret_key_here
  ```
* 이후에는 코드 실행 시 자동으로 해당 키가 로드되어 정상 동작합니다.

```
