wagon = [0] * int(input())

while True:
    command = input().split()
    current_command = command[0]
    if current_command == 'End':
        print(wagon)
        break

    elif current_command == 'add':
        number_of_people = int(command[1])
        wagon[-1] += number_of_people
    elif current_command == 'insert':
        position = int(command[1])
        number_of_people = int(command[2])
        wagon[position] += number_of_people
    elif current_command == 'leave':
        position = int(command[1])
        number_of_people = int(command[2])
        wagon[position] -= number_of_people






