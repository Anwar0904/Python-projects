import json
from pathlib import Path


def message_loader(path: str | Path) -> list[dict]:
    path = Path(path)
    with path.open(encoding="utf-8") as file:
        data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Expected a json list")
        if not all(isinstance(item, dict) for item in data):
            raise ValueError("Every message must be a JSON object.")
        return data


# print(message_loader(path=Path(__file__).with_name("message.json")))
