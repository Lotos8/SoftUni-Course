
old_list_numbers =  input().split()
numbers = []
for number in range(len(old_list_numbers)):
    numbers.append(int(old_list_numbers[number]))
while True:
    command = input().split()

    if command[0] == 'Finish':
        break

    if command[0] == 'Add':
        value = command[1]
        numbers.append(value)
    elif command[0] == 'Remove':
        value_is_there = int(command[1])
        if value_is_there in numbers:
            numbers.remove(value_is_there)
    elif command[0] == 'Replace':
        value = int(command[1])
        replacement_value = command[2]
        if value in numbers:
            index_value = numbers.index(value)
            numbers[index_value] = replacement_value
    elif command[0] == 'Collapse':
        compering_value = int(command[1])
        numbers = [x for x in numbers if x >= compering_value]

print(' '.join(map(str, numbers)))