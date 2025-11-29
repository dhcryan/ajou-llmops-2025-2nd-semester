"""Small helper that fires multiple /chat requests for testing/logging."""

import argparse
import asyncio
from typing import List

import httpx

SAMPLE_MESSAGES = [
    "LLMOps가 뭐야?",
    "프롬프트 버전 관리를 어떻게 자동화할까?",
    "지연시간을 줄이려면 어떤 모니터링 지표를 봐야 할까?",
    "사용자 피드백을 프롬프트 튜닝에 연결하는 방법?",
    "토큰 사용량과 비용을 예측하려면?",
    "운영 환경에서 롤백 전략은 어떻게 세울까?",
]


async def send_messages(url: str, prompt_versions: List[str]) -> None:
    async with httpx.AsyncClient(timeout=30) as client:
        for idx, message in enumerate(SAMPLE_MESSAGES):
            payload = {
                "message": message,
                "prompt_version": prompt_versions[idx % len(prompt_versions)],
            }
            response = await client.post(url, json=payload)
            response.raise_for_status()
            body = response.json()
            print(f"[{payload['prompt_version']}] {body['reply'][:60]}...")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--url",
        default="http://127.0.0.1:8000/chat",
        help="Chat endpoint URL",
    )
    parser.add_argument(
        "--prompt-versions",
        nargs="+",
        default=["v1", "v2"],
        help="Prompt versions to cycle through",
    )
    args = parser.parse_args()
    asyncio.run(send_messages(args.url, args.prompt_versions))


if __name__ == "__main__":
    main()
