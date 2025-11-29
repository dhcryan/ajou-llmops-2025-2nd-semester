"""Utility for persisting LLM call metadata to CSV."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from .schemas import LogRecord

DEFAULT_LOG_PATH = Path(__file__).resolve().parents[1] / "logs" / "llm_responses.csv"
CSV_HEADERS = [
    "timestamp",
    "message",
    "prompt_version",
    "model",
    "latency_ms",
    "total_tokens",
    "provider",
]


class CSVChatLogger:
    """Append-only CSV logger for LLM metadata."""

    def __init__(self, log_path: Path | str = DEFAULT_LOG_PATH):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: LogRecord) -> None:
        """Append a log record, writing the header if necessary."""

        write_header = not self.log_path.exists()
        row = record.dict()
        with self.log_path.open("a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADERS)
            if write_header:
                writer.writeheader()
            writer.writerow(row)

    def iter_logs(self) -> Iterable[LogRecord]:
        """Yield log entries from the CSV file if it exists."""

        if not self.log_path.exists():
            return
        with self.log_path.open("r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield LogRecord(**row)
