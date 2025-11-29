"""FastAPI entrypoint for the mini-chatbot assignment."""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool

from .llm_client import LLMClient
from .logger import CSVChatLogger
from .schemas import ChatRequest, ChatResponse, LogRecord

app = FastAPI(title="Mini Chatbot API", version="0.1.0")
llm_client = LLMClient()
logger = CSVChatLogger()


@app.get("/healthz")
def healthcheck() -> dict:
    """Simple readiness endpoint."""

    return {"status": "ok", "provider": llm_client.provider}


@app.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest) -> ChatResponse:
    """Handle chatbot requests by delegating to the LLM client."""

    result = await run_in_threadpool(
        llm_client.generate_response,
        payload.message,
        payload.prompt_version,
        payload.model,
    )
    timestamp = datetime.now(timezone.utc)
    log_record = LogRecord(
        timestamp=timestamp,
        message=payload.message,
        prompt_version=payload.prompt_version,
        model=result.model,
        latency_ms=result.latency_ms,
        total_tokens=result.total_tokens,
        provider=result.provider,
    )
    logger.append(log_record)
    return ChatResponse(
        reply=result.reply,
        model=result.model,
        prompt_version=payload.prompt_version,
        latency_ms=result.latency_ms,
        total_tokens=result.total_tokens,
        timestamp=timestamp,
    )
