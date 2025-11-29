# Assignment03 – Mini Chatbot API + LLMOps 로그

이 디렉터리는 9·10주차 통합 과제를 위한 FastAPI 기반 미니 챗봇과 LLMOps 로깅/분석 예시를 담고 있습니다. 주요 구성 요소는 아래와 같습니다.

- `app/` – FastAPI 앱, LLM 클라이언트, CSV 로거
- `logs/llm_responses.csv` – API 호출이 기록되는 로그
- `scripts/send_requests.py` – 테스트용 요청 배치 스크립트
- `analyze_logs.py` – 로그 통계 계산 스크립트
- `reports/` – 실험 요약 문서

## 1. FastAPI 서버 실행

```bash
uvicorn assignment03.app.main:app --reload
```

엔드포인트

- `GET /healthz` – 서버/LLM 준비 상태 확인
- `POST /chat` – 챗봇 응답. 요청/응답 예시는 아래와 동일합니다.

요청 예시

```json
{
  "message": "LLMOps가 뭐야?",
  "prompt_version": "v1"
}
```

응답 예시 (기본 스텁 모델 기준)

```json
{
  "reply": "질문: LLMOps가 뭐야?\n핵심 요약: ...",
  "model": "gpt-4o-mini-stub",
  "prompt_version": "v1",
  "latency_ms": 120,
  "total_tokens": 118,
  "timestamp": "2024-11-25T12:00:07.120000+00:00"
}
```

> **LLM 연동**
>
> - `OPENAI_API_KEY`가 설정되어 있으면 OpenAI Chat Completions API를 사용합니다.
> - 키가 없으면 규칙 기반 스텁 모델이 실행되어 토큰/지연시간을 근사치로 기록합니다.

## 2. 로그 수집 포맷

모든 호출은 `logs/llm_responses.csv`에 아래 필드로 누적됩니다.

| column | 설명 |
| --- | --- |
| `timestamp` | UTC 시각 |
| `message` | 사용자 메시지 |
| `prompt_version` | 프롬프트 버전 (v1/v2 등) |
| `model` | 사용 모델명 (스텁일 경우 `-stub` 접미사) |
| `latency_ms` | 처리 지연(ms) |
| `total_tokens` | 총 토큰 수 (스텁은 추정치) |
| `provider` | `openai` 또는 `stub` |

## 3. 샘플 요청 보내기

다음 스크립트는 서버에 6회 이상 요청하여 로그를 쌓습니다.

```bash
python assignment03/scripts/send_requests.py --url http://127.0.0.1:8000/chat
```

`--prompt-versions v1 v2` 옵션으로 버전을 번갈아가며 보낼 수 있습니다.

## 4. 통계/비교

기록된 로그는 `analyze_logs.py`로 바로 분석할 수 있습니다.

```bash
python assignment03/analyze_logs.py
```

출력 예시

```
Prompt version stats:
            calls  avg_latency_ms  avg_tokens
prompt_version                               
v1              4          106.25      144.0
v2              4          148.00      163.0

Model stats:
                    calls  avg_latency_ms
model                                    
gpt-4o-mini-stub      8          127.12
```

## 5. 리포트

`reports/` 이하에 API 설명, 로그 분석 표, 간단 인사이트를 작성했습니다. 제출 시 요구하는 **로그 CSV**와 **요약 문서**를 그대로 첨부하면 됩니다.
