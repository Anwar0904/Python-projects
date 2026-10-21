# Day 3 — Python Exceptions, JSON & Logging

try:
    number = 10
    result = 10 / 1
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Division completed result: {result}")
finally:
    print("1st Program finished")

# try:
#     result = int("hello")
# except ValueError as e:
#     print(f"something went wrong{e}")

# print("2nd Program finished")


# Raise in python
age = -6
if age < 5:
    raise ValueError("Age cann't be negative")
else:
    print("age:", age)
