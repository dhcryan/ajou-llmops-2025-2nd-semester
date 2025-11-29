"""LLM client abstraction with a graceful stub fallback."""

from __future__ import annotations

import os
import random
import textwrap
import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class LLMResult:
    reply: str
    model: str
    latency_ms: int
    total_tokens: Optional[int]
    provider: str


class LLMClient:
    """Produces chatbot replies using OpenAI or a local stub."""

    def __init__(self, default_model: str = "gpt-4o-mini") -> None:
        self.default_model = default_model
        self.provider = "stub"
        self._client = None
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            try:
                from openai import OpenAI

                self._client = OpenAI(api_key=api_key)
                self.provider = "openai"
            except Exception:  # pragma: no cover - best effort import guard
                self._client = None
                self.provider = "stub"

    def _system_prompt(self, prompt_version: str) -> str:
        templates = {
            "v1": textwrap.dedent(
                """
                당신은 학습자를 돕는 조교입니다. 질문의 요점만 간결히 설명하세요.
                필요하면 예시를 한 개 정도만 포함합니다.
                """
            ).strip(),
            "v2": textwrap.dedent(
                """
                당신은 LLMOps 전문가입니다. 배경 설명과 운영 팁을 2~3문장으로 추가하세요.
                중요한 용어는 **굵게** 강조합니다.
                """
            ).strip(),
        }
        return templates.get(prompt_version, templates["v1"])

    def generate_response(
        self, message: str, prompt_version: str, model: Optional[str] = None
    ) -> LLMResult:
        model_name = model or self.default_model
        start = time.perf_counter()
        if self.provider == "openai" and self._client is not None:
            response = self._client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": self._system_prompt(prompt_version)},
                    {"role": "user", "content": message},
                ],
            )
            reply = response.choices[0].message.content
            total_tokens = (
                response.usage.total_tokens if getattr(response, "usage", None) else None
            )
            used_model = model_name
        else:
            reply = self._stub_reply(message, prompt_version)
            total_tokens = self._estimate_tokens(message, reply)
            used_model = f"{model_name}-stub"
            time.sleep(random.uniform(0.05, 0.2))
        latency_ms = int((time.perf_counter() - start) * 1000)
        return LLMResult(
            reply=reply,
            model=used_model,
            latency_ms=latency_ms,
            total_tokens=total_tokens,
            provider=self.provider,
        )

    def _stub_reply(self, message: str, prompt_version: str) -> str:
        random.seed(hash(message + prompt_version) % (2**32))
        insights = [
            "데이터 파이프라인의 병목을 먼저 측정하세요.",
            "프롬프트 버전 관리가 실험 속도를 결정합니다.",
            "짧은 피드백 루프가 운영 품질을 높입니다.",
            "토큰 사용량과 지연시간을 함께 살펴보세요.",
        ]
        template = (
            "v2"
            if prompt_version.lower().startswith("v2")
            else "v1"
        )
        if template == "v2":
            reply = (
                f"{message.strip()} 질문에 대한 운영 팁입니다. "
                f"{random.choice(insights)} **LLMOps**에서 자주 쓰이는 기법입니다."
            )
        else:
            reply = (
                f"질문: {message.strip()}\n"
                f"핵심 요약: {random.choice(insights)}"
            )
        return reply

    @staticmethod
    def _estimate_tokens(message: str, reply: str) -> int:
        token_estimate = int(1.3 * (len(message.split()) + len(reply.split())))
        return max(token_estimate, 1)
