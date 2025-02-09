import re
from re import match

phone_numbers = input()
pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(pattern, phone_numbers)

for i in range(len(matches)):
    if i < len(matches) - 1:
        print(matches[i], end=', ')
    else:
        print(matches[i])