text = input()
# text = text.replace(" ", "")
text = [char for char in text if char != " "]
occurrences = {}

for char in text:
    if char not in occurrences.keys():
        occurrences[char] = 0
    occurrences[char] += 1
for key, value in occurrences.items():
    print(f"{key} -> {value}")
