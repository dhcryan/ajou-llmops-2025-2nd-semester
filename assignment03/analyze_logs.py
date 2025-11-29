"""Simple utility to compute descriptive stats from the CSV logs."""

from pathlib import Path

import pandas as pd

LOG_PATH = Path(__file__).resolve().parent / "logs" / "llm_responses.csv"


def main() -> None:
    if not LOG_PATH.exists():
        raise SystemExit(f"Log file not found: {LOG_PATH}")
    df = pd.read_csv(LOG_PATH, parse_dates=["timestamp"])
    if df.empty:
        raise SystemExit("Log file is empty.")

    version_stats = (
        df.groupby("prompt_version")
        .agg(
            calls=("message", "count"),
            avg_latency_ms=("latency_ms", "mean"),
            avg_tokens=("total_tokens", "mean"),
        )
        .sort_index()
    )
    model_stats = (
        df.groupby("model")
        .agg(
            calls=("message", "count"),
            avg_latency_ms=("latency_ms", "mean"),
        )
        .sort_values(by="avg_latency_ms")
    )

    print("Prompt version stats:\n", version_stats.round(2), "\n", sep="")
    print("Model stats:\n", model_stats.round(2), sep="")


if __name__ == "__main__":
    main()
