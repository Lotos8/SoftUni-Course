
# if 6 > len(password) or len(password) > 10:
#     print("Password must be between 6 and 10 characters")
# if not isalnum(password):
#     print("Password must consist only of letters and digits")
# if isdigit(password) < 2:
#     print("Password must contain at least 2 digits")

# if 6 > len(password) or len(password) > 10:
#     print("Password must be between 6 and 10 characters")
# for char in range(len(password)):
#     if password[char].isalnum():
#         continue
#     else:
#         print("Password must consist only of letters and digits")
#         break
# for digit in range(len(password)):
#     if password[digit].isdigit() >= 2:
#         continue
#     else:
#         print("Password must contain at least 2 digits")
#         break
def password_validator(word):
    error_messages = []
    if len(word) < 6 or len(word) > 10:
        error_messages.append("Password must be between 6 and 10 characters")
    if not word.isalnum():
        error_messages.append("Password must consist only of letters and digits")
    digits_count = 0
    for digit in word:
        if digit.isdigit():
            digits_count += 1
    if digits_count < 2:
        error_messages.append("Password must have at least 2 digits")
    return error_messages


password = input()
all_errors = password_validator(password)
if all_errors:
        print("\n".join(all_errors))
else:
    print("Password is valid")
