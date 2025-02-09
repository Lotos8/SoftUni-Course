current_string = input()
while current_string != 'End':
    if current_string != 'SoftUni':
       # new_string = ''
       # new_string += character * 2
        for character in current_string:
            print(character * 2, end= '')
        print()



    current_string = input()