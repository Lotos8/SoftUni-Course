# def absolute_value(num: int):
#     for abs_num in number_list:
#         current_list_abs.append(abs(int(abs_num)))
#     return current_list_abs
#
#
# current_list_abs = []
# number_list = [number for number in input().split(' ')]
# print(' '.join(map(str, current_list_abs)))
my_list = [2, 4, [6, 8, [10, 12, [14, 16]]]]
result = my_list[2][2][2][1]
my_list[2][2].append(18)
flattened = sum([i if isinstance(i, list) else [i] for i in my_list[2][2]], [])
final_result = flattened[-2]
print(result, final_result)

def password_validator(some_password: str) -> list:
    list_with_error_messages = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_with_error_messages.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_with_error_messages.append("Password must consist only of letters and digits")
    digits_found = 0
    for current_character in some_password:
        if current_character.isdigit():
            digits_found += 1
    if digits_found < 2:
        list_with_error_messages.append("Password must have at least 2 digits")
    return list_with_error_messages
