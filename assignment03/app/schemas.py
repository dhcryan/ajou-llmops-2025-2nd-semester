"""Pydantic schemas for the assignment03 FastAPI app."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Incoming payload for the /chat endpoint."""

    message: str = Field(..., description="사용자가 보낸 자연어 메시지")
    prompt_version: str = Field(
        "v1",
        description="프롬프트 템플릿 버전. A/B 테스트 용도로 사용",
        pattern=r"^v[0-9]+",
    )
    model: Optional[str] = Field(
        None, description="사용할 LLM 모델 이름. 지정하지 않으면 기본 모델 사용"
    )


class ChatResponse(BaseModel):
    """Successful response payload."""

    reply: str
    model: str
    prompt_version: str
    latency_ms: int
    total_tokens: Optional[int]
    timestamp: datetime


class LogRecord(BaseModel):
    """Row stored in the CSV log."""

    timestamp: datetime
    message: str
    prompt_version: str
    model: str
    latency_ms: int
    total_tokens: Optional[int]
    provider: str
