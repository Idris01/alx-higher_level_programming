#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
last_digit = -last_digit if number < 0 else last_digit
status = ""

if last_digit > 5:
    status = "greater than 5"
elif last_digit == 0:
    status = "0"
else:
    status = "less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} and is {status}")
