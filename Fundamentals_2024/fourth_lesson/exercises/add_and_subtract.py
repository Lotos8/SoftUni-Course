def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2


def subtract(result: int, num3: int) -> int:
    return result - num3


def add_and_subtract(first: int, second: int, third: int) -> int:
    first_operation = sum_numbers(first, second)
    final_operation = subtract(first_operation, third)
    return final_operation


first_number = int(input())
second_lesson = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_lesson, third_number))
