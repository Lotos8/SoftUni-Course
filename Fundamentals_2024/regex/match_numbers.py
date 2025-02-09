import re
from sys import flags

numbers_ = input()

find_numbers = re.sub(r'(?<=^|\s)-?\d+(\.\d+)?','" "',numbers_,flags=re.MULTILINE)
matches = re.findall(find_numbers, numbers_)

print(find_numbers)