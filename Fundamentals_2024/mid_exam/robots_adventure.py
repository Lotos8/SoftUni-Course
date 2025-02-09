adventure = list(map(int, input().split('|')))
collect = 0
print(adventure)
while True:
    commands = input().split('$')


    if commands[0] == 'Adventure over':
        break

    step = commands[0]

    if step == "Step Backward":
        start_index = int(commands[1])
        steps = int(commands[2])
        if 0 <= start_index <= len(adventure):
            specific_direction = (start_index - steps) % len(adventure)
            collect += adventure[specific_direction]
            adventure[specific_direction] = 0
    elif step == "Step Forward":
        start_index = int(commands[1])
        steps = int(commands[2])
        if 0 <= start_index <= len(adventure):
            specific_direction = (start_index + steps) % len(adventure)
            collect += adventure[specific_direction]
            adventure[specific_direction] = 0
    double = step.split()
    if double[0] == "Double":
        index = int(double[1])
        if 0 <= index <= len(adventure):
            adventure[index] *= 2
    elif step == "Switch":
        adventure.reverse()

print('-'.join(map(str, adventure)))
print(f"Robo finished the adventure with {collect} items!")