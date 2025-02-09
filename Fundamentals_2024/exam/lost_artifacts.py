import re
text = input()

find_name = r'([A-Z\sa-z]+)'
find_numbers = r'(-?\d+\.?\d*,-?\d+\.?\d*)'

messege_pattern = fr'{find_name}.*?{find_numbers}'

matches = re.finditer(messege_pattern, text)

if matches:
    for match in matches:
        name = match.group(1).strip()
        cordinates = match.group(2).strip()

        print(f"Found {name} at coordinates {cordinates}.")
else:
    print("No valid artifacts found.")