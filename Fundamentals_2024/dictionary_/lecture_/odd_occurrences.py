words = input().split(' ')
elements = {}

for word in words:
    words_lower = word.lower()
    if words_lower not in elements:
        elements[words_lower] = 0
    elements[words_lower] += 1
for key, value in elements.items():
    if value % 2 != 0:
        print(key, end=" ")