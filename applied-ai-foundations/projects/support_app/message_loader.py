import json
from pathlib import Path


def load_messages(path: str | Path) -> list[dict]:
    path = Path(path)
    with path.open(encoding="utf-8") as file:
        data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Expected a json list")
        if not all(isinstance(item, dict) for item in data):
            raise ValueError("Every message must be a JSON object.")
        return data
