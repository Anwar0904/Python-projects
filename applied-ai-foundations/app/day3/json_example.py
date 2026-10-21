import json
from pathlib import Path

text = '{"name":"Ali","age":22}'

data = json.loads(text)
# print(data["name"])

py_data = {"name": "ali", "age": 22}

json_text = json.dumps(py_data)
print(json_text)


# path = Path("message.json")
# with path.open(encoding="utf-8") as file:
#     data = json.loads(file)


# Structural and syntax validation

print(isinstance(py_data, dict))
if not isinstance(py_data, dict):
    raise ValueError("Expected a json data")
else:
    print("json data")

# all() keyword

numbers = [1, 3, 5, 7]
result = all(num % 2 != 0 for num in numbers)

print(result)
