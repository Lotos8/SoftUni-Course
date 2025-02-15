# 1
first_number = int(input())
second_number = int(input())
third_number = int(input())
forth_number = int(input())
result = (first_number + second_number) // third_number * forth_number
print(result)

# 2
first_character = input()
second_character = input()
third_character = input()
print(f"{first_character}{second_character}{third_character}")
# result = first_character + second_character + third_character
# print(result)


# 3

from math import ceil

persons = int(input())
capacity = int(input())
courses = ceil(persons / capacity)
print(courses)

# 4

number_of_characters = int(input())
total_sum = 0
for character in range(number_of_characters):
    current_character = input()
    total_sum += ord(current_character)
print(f"The sum equals: {total_sum}")

# 5

start_index = int(input())
final_index = int(input())
for index in range(start_index, final_index + 1):
    if index == final_index:
        print(chr(index))
    else:
        print(chr(index), end=" ")

# 6

number_of_symbols = int(input())
for first_symbol in range(97, 97 + number_of_symbols):
    for second_symbol in range(97, 97 + number_of_symbols):
        for third_symbol in range(97, 97 + number_of_symbols):
            print(f"{chr(first_symbol)}{chr(second_symbol)}{chr(third_symbol)}")

# 7

number_of_lines = int(input())
tank_capacity = 255
for line in range(number_of_lines):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0:  # not enough capacity
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water
print(255 - tank_capacity)

# 8

number_of_companions = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        number_of_companions -= 2
    if current_day % 15 == 0:
        number_of_companions += 5
    if current_day % 3 == 0:
        coins -= 3 * number_of_companions
    if current_day % 5 == 0:
        coins += 20 * number_of_companions
        if current_day % 3 == 0:  # motivation party
            coins -= 2 * number_of_companions
    coins += 50
    coins -= 2 * number_of_companions
coins_per_companion = coins // number_of_companions
print(f"{number_of_companions} companions received {coins_per_companion} coins each.")

# 9

number_of_snowballs = int(input())
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_value = 0
max_snowball_quality = 0
for current_snowball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight // current_time) ** current_quality
    if current_value > max_snowball_value:
        max_snowball_weight = current_weight
        max_snowball_time = current_time
        max_snowball_quality = current_quality
        max_snowball_value = current_value
print(f"{max_snowball_weight} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})")

# 10

number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // (2 * 3)
total_armor_broken = total_shield_broken // 2
expenses = total_helmet_broken * helmet_price \
           + total_sword_broken * sword_price \
           + total_shield_broken * shield_price \
           + total_armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
