# Day 1 — Think in Python

from collections import Counter

messages = [
    {"id": 1, "text": "  I need a refund  "},
    {
        "id": 2,
        "text": "My account is locked lorem dkad fldjfladjf d;jfadsjfsd fj fldsjf  asdf ;lkj asdf ;lkj asdf ;lkj asdf ;",
    },
    {"id": 3, "text": "   "},
    {"id": 4, "text": "I need a refund"},
]

# print(messages)
clean_messages = []

for message in messages:
    cleaned_text = message["text"].strip()

    if cleaned_text:
        clean_messages.append({"id": message["id"], "text": cleaned_text})
# print(clean_messages)


# Exercise

## 1. count valid and empty messages

valid_count = 0
empty_count = 0
for message in clean_messages:
    if message["text"]:
        valid_count += 1
    else:
        empty_count += 0
print(f"{valid_count}\n{empty_count}")


## 2. Collect messages longer than 50 characters.

longer_messages = []

for message in messages:
    if len(message["text"]) >= 50:
        longer_messages.append(message)

# print(longer_messages)


## 3.Find duplicate message texts.

msg_counter = Counter(message["text"] for message in clean_messages)

duplicate_messages = {text: count for text, count in msg_counter.items() if count > 1}

# print(duplicate_messages)


# 4. Explain the difference between an empty string, a missing dictionary key, and None.

# The string with no value in it is called emply string e.g. name="".  if there is no key,value defined in dictionary and if tried to retreive so it is reffered as missing dictionary key. and None is a data type ass null in js which says a corresponding varaible is having nothing in it
