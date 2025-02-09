import re

names = input()
regex_ = r'\b([A-Z][a-z]+ [A-Z][a-z]+\b)'
matches_ = re.findall(regex_, names)

print(" ".join(matches_))