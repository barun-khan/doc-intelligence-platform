import json
import os
from datetime import datetime

# The log file lives in the project root
_LOG_PATH = "audit_log.jsonl"


def log_interaction(question: str, answer: str, sources: list[str]) -> None:
    """Append one question/answer/sources record to the audit log."""
    record = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer,
        "sources": sources,
    }

    # Open in append mode ("a") so we add to the file, never overwrite it
    with open(_LOG_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")