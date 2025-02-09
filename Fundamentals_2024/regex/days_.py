import re

dates_ = input()

dates_founds = r'\b(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})\b'
matches = re.findall(dates_founds, dates_)

for match in matches:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')

