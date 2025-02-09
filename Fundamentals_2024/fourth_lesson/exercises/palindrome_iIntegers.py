# def palindrome_integers(number):
#     for num in number:
#         backward_num = num[::-1]
#         if int(num) == int(backward_num):
#             print('True')
#
#         else:
#             print('False')
#
#
# palindrome_integers(input().split(','))
#
def palindrome_integ(numbers: str) -> bool:
    return numbers == numbers[::-1]


number = input().split(', ')
for num in number:
    print(palindrome_integ(num))



