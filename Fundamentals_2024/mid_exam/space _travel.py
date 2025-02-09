travel_route = input().split('||')
amount_of_fuel = int(input())
amount_of_ammunition = int(input())
fuel = 0
for i in range(len(travel_route)):
    route = travel_route[i].split()
    command = route[0]

    if command == 'Titan':
        print("You have reached Titan, all passengers are safe." )
        break

    if command == 'Travel':
        light_years = int(route[1])
        fuel = light_years * 1
        amount_of_fuel -= fuel
        if 0 <= amount_of_fuel:
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == 'Enemy':
        if amount_of_ammunition >= int(route[1]):
            amount_of_ammunition -= int(route[1])
            print(f"An enemy with {int(route[1])} armour is defeated.")
        else:
            spent_fuel = int(route[1]) * 2
            if amount_of_fuel >= spent_fuel:
                amount_of_fuel -= spent_fuel
                print(f"An enemy with {route[1]} armour is outmaneuvered.")
            else:
                print("Mission failed." )
                break
    elif command == 'Repair':
        add_fuel = int(route[1])
        add_ammunitions = int(route[1]) * 2
        amount_of_ammunition += add_ammunitions
        print(f"Ammunitions added: {add_ammunitions}.")
        print(f"Fuel added: {add_fuel}.")
