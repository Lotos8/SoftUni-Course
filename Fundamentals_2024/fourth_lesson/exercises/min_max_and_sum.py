# def min_max_add_value():
#     numbers = list(map(int, input().split()))
#     min_value = min(numbers)
#     max_value = max(numbers)
#     add_value = sum(numbers)
#     print(f"The minimum number is {min_value}")
#     print(f"The maximum number is {max_value}")
#     print(f"The sum number is: {add_value}")
#
#
# min_max_add_value()

def min_value(numbers):
    return f"The minimum number is {min(numbers)}"


def max_value(numbers):
    return f"The maximum number is {max(numbers)}"


def sum_value(numbers):
    return f"The sum number is: {sum(numbers)}"


numbers_of_list = list(map(int, input().split()))
print(min_value(numbers_of_list))
print(max_value(numbers_of_list))
print(sum_value(numbers_of_list))

