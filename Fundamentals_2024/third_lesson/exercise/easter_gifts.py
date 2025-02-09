gifts = input().split()
command = input()

while not command == "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for i in range(len(gifts)):
            if command[1] in gifts[i]:
                gifts[i] = "None"
    elif "Required" in command:
        for i in range(len(gifts)):
            if i == int(command[2]):
                gifts[i] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[1]
    command = input()
while "None" in gifts:
    gifts.remove("None")
for i in gifts:
    print(i, end=" ")

# list_with_gifts = input().split()
# command = input()
# while command != 'No Money':
#     command = command.split()
#     if "OutOfStock" in command:
#         for i in range(len(list_with_gifts)):
#             if command[1] in list_with_gifts[i]:
#                 list_with_gifts[i] = 'None'
#     elif "Required" in command:
#         for i in range(len(list_with_gifts)):
#             if i == int(command[2]):
#                 list_with_gifts[i] = command[1]
#     elif "JustInCase" in command:
#         list_with_gifts[-1] = command[1]
#
#     command = input()
# while 'None' in list_with_gifts:
#     list_with_gifts.remove('None')
# my_string = " "
# for a in list_with_gifts:
#     my_string = my_string + ' ' + a
# print(my_string)
#
