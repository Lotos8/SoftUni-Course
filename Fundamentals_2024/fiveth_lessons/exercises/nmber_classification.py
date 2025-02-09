numbers = list(map(int, input().split(', ')))
positive_num = [int(num) for num in numbers if num >= 0]
negative_num = [int(num) for num in numbers if num < 0]
even_num = [int(num) for num in numbers if num % 2 == 0]
odd_num = [int(num) for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(map(str, positive_num))}")
print(f"Negative: {', '.join(map(str, negative_num))}")
print(f"Even: {', '.join(map(str, even_num))}")
print(f"Odd: {', '.join(map(str, odd_num))}")