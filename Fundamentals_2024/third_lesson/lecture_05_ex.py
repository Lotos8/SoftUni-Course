n = int(input())

number = []

for _ in range(n):
    current_number = int(input())
    number.append(current_number)
command = input()

filtered_number = []

if command == 'odd':
    for num in number:
        if num % 2 != 0:
            filtered_number.append(num)
elif command == 'even':
    for num in number:
        if num % 2 == 0:
            filtered_number.append(num)
elif command == 'positive':
    for num in number:
        if num >= 0:
            filtered_number.append(num)
