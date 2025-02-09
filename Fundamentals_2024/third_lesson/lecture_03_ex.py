n = int(input())
positive = []
negative = []

for _ in range(n):
    current_number = int(input())

    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

counter_of_positive_numbers = len(positive)
sum_of_negative_number = sum(negative)

print()
print()
print()
print()