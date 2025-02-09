number_of_string = int(input())
for strings in range(number_of_string):
    current_string = input()
    if ',' in current_string or \
        '.' in current_string or \
        '_' in current_string:
        print()
    else:
        pass
