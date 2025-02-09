list_of_friends = [i for i in input().split()]
blacklist_friend_count = 0
lost_names_count = 0
commands = []
#it wrong try again
while True:
    command = input().split()

    if command[0] == 'Report':
        break
    commands.append(command)
    if command[0] == 'Blacklist':
        name = command[1]
        if name in list_of_friends:
            blacklist_friend_count += 1
            index = list_of_friends.index(name)
            list_of_friends[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
           print(f"{name} was not found.")
    elif command[0] == 'Error':
        index = int(command[1])
        if 0 <= index < len(list_of_friends) and list_of_friends[index] not in ["Blacklisted", "Lost"]:
            print(f"{list_of_friends[index]} was lost due to an error.")
            list_of_friends[index] = "Lost"
            lost_names_count += 1
    elif command[0] == 'Change':
        index = int(command[1])
        name = command[2]
        if 0 <= index <= len(list_of_friends):
            current_name = list_of_friends[index]
            list_of_friends[index] = name
            print(f"{name} changed his username to {list_of_friends[index]}.")

print(f"Blacklisted names: {blacklist_friend_count}")
print(f"Lost names: {lost_names_count}")
print(' '.join(list_of_friends))
