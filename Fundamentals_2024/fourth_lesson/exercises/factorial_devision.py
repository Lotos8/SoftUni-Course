def factorial_division(number: int):
    multiply_num = number
    for num in range(1, number):
        multiply_num *= num
    return multiply_num


factorial_num = int(input())
division_num = int(input())
first_factorial_num = factorial_division(factorial_num)
first_division_num = factorial_division(division_num)
result = first_factorial_num / first_division_num
print(f"{result:.2f}")
