import re
from typing import Literal

categories = Literal["billings", "technical", "general", "sales"]


def route_message(text: str) -> categories:
    word = set(re.findall(r"\b\w+\b", text.casefold()))
    if word & {"refund", "payment", "invoice"}:
        return "billings"
    if word & {"error", "crash", "login", "crashing"}:
        return "technical"
    else:
        return "general"
