targets_list = list(map(int, input().split('|')))
target_point = 0

while True:
    commands = list(map(str, input().split('@')))
    stop_index = 0
    if commands[0] == 'Game over':
        break

    shoot = commands[0]

    if shoot == 'Shoot Left':
        start_index = int(commands[1])
        length = int(commands[2])
        if 0 <= start_index <= len(targets_list):
                stop_index = (start_index - length) % len(targets_list)
                if targets_list[stop_index] < 5:
                    target_point += targets_list[stop_index]
                    targets_list[stop_index] = 0
                else:
                    target_point += 5
                    targets_list[stop_index] -= 5

    elif shoot == 'Shoot Right':
        start_index = int(commands[1])
        length = int(commands[2])
        if 0 <= start_index <= len(targets_list):
            stop_index = (start_index + length) % len(targets_list)
            if targets_list[stop_index] < 5:
                target_point += targets_list[stop_index]
                targets_list[stop_index] = 0
            else:
                target_point += 5
                targets_list[stop_index] -= 5

    elif shoot == 'Reverse':
        targets_list.reverse()

print(' - '.join(list(map(str, targets_list))))
print(f"John finished the archery tournament with {target_point} points!")