
registered_dict = {}
counter = int(input())
for _ in range(counter):
    commands = input().split()
    name = commands[1]
    if commands[0] == 'register':
        number_plate = commands[2]
        if name not in registered_dict:
            registered_dict[name] = number_plate
            print(f"{name} registered {number_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {number_plate}")
    elif commands[0] == 'unregister':
        if name not in registered_dict:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del registered_dict[name]


for username, licence_car_plate in registered_dict.items():
    print(f"{username} => {licence_car_plate}")