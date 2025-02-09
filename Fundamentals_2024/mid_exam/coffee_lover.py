coffee_list = input().split()
numbers_of_command = int(input())
#not finish yet
for command in range(1, numbers_of_command + 1):
    command_ = input().split()

    if command_[0] == 'Include':
        coffee = command_[1]
        coffee_list.append(coffee)
    elif command_[0] == 'Remove':
        location_of_coffee = command_[1]
        index = int(command_[2])
        if location_of_coffee == 'first':
            if index <= len(coffee_list):
                coffee_list = coffee_list[index:]
        elif location_of_coffee == 'last':
            if index <= len(coffee_list):
                coffee_list = coffee_list[:-index]
    elif command_[0] == 'Prefer':
        #slop them if they exist
        first_coffee_index = int(command_[1])
        second_coffee_index = int(command_[2])
        if  0 <= int(first_coffee_index) <= len(coffee_list) and 0 <= int(second_coffee_index) <= len(coffee_list):
            coffee_list[first_coffee_index], coffee_list[second_coffee_index] = coffee_list[second_coffee_index], coffee_list[first_coffee_index]
    elif command_[0] == 'Reverse':
        #reverse our list
        coffee_list.reverse()

print(' '.join(coffee_list))

# def manage_coffee_list(coffee_list, n, commands):
#     # Process each command
#     for command in commands:
#         parts = command.split()
#         action = parts[0]
#
#         if action == "Include":
#             coffee = parts[1]
#             coffee_list.append(coffee)
#
#         elif action == "Remove":
#             position = parts[1]
#             number_of_coffees = int(parts[2])
#             if position == "first":
#                 if number_of_coffees <= len(coffee_list):
#                     coffee_list = coffee_list[number_of_coffees:]
#             elif position == "last":
#                 if number_of_coffees <= len(coffee_list):
#                     coffee_list = coffee_list[:-number_of_coffees]
#
#         elif action == "Prefer":
#             index1 = int(parts[1])
#             index2 = int(parts[2])
#             if 0 <= index1 < len(coffee_list) and 0 <= index2 < len(coffee_list):
#                 # Swap the coffees at index1 and index2
#                 coffee_list[index1], coffee_list[index2] = coffee_list[index2], coffee_list[index1]
#
#         elif action == "Reverse":
#             coffee_list.reverse()
#
#     # Print the final list of coffees
#     print("Coffees:")
#     print(" ".join(coffee_list))
#
#
# # Example input
# initial_coffees = input().split()
# n = int(input())
# commands = [input() for _ in range(n)]
#
# # Manage coffee list based on commands
# manage_coffee_list(initial_coffees, n, commands)