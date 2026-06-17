import os

number = int(os.getenv("NUMBER", "0"))

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
