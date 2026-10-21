import json
from pathlib import Path
from message_loader import message_loader

try:
    messages = message_loader(path=Path(__file__).with_name("message.json"))
except FileNotFoundError as e:
    print("file not found")
except json.JSONDecodeError as e:
    print("file contain invlid json formate")
except ValueError as e:
    print(f"invalid message data : {e}")
else:
    print(messages)
