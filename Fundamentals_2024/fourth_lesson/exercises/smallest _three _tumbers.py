def get_smaller_number(number: list) -> int:
    return min(number)


first_number = int(input())
second_number = int(input())
third_number = int(input())
list_of_numbers = [first_number, second_number, third_number]
print(get_smaller_number(list_of_numbers))