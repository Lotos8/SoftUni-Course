# # 1
# list_with_numbers = input().split()
# opposite_numbers = []
# for number in list_with_numbers:
#     opposite_number = -int(number)
#     opposite_numbers.append(opposite_number)
# print(opposite_numbers)
#
# # print([-int(number) for number in input().split()])
#
#
# # 2
# factor = int(input())
# count = int(input())
# numbers = []
# for multiplier in range(1, count + 1):
#     numbers.append(factor * multiplier)
# print(numbers)
#
# # 3
# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# game_was_terminated = False
# players = input().split()
# for player in players:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_was_terminated = True
#         break
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if game_was_terminated:  # if game was terminated == True
#     print("Game was terminated")
#
# # 3.1
# team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# game_was_terminated = False
# players = input().split()
# for player in players:
#     team, number = player.split("-")
#     if int(number) in team_a:
#         team_a.remove(int(number))
#     elif int(number) in team_b:
#         team_b.remove(int(number))
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_was_terminated = True
#         break
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if game_was_terminated:  # if game was terminated == True
#     print("Game was terminated")
#
# # 4
#
# money_as_string = input().split(", ")
# number_of_beggars = int(input())
# # money_as_integer = [int(money) for money in money_as_string]
# money_as_integer = []
# for money in money_as_string:
#     money_as_integer.append(int(money))
# list_with_beggars_sums = []
# start_index = 0
# for current_beggar in range(number_of_beggars):
#     current_beggar_sum = 0
#     for current_index in range(start_index, len(money_as_integer), number_of_beggars):
#         current_beggar_sum += money_as_integer[current_index]
#     list_with_beggars_sums.append(current_beggar_sum)
#     start_index += 1
# print(list_with_beggars_sums)
#
# # 5
#
# deck_of_cards = input().split()
# count_of_shuffles = int(input())
# for current_shuffle in range(count_of_shuffles):
#     middle_of_the_deck = len(deck_of_cards) // 2
#     left_part = deck_of_cards[:middle_of_the_deck]
#     right_part = deck_of_cards[middle_of_the_deck:]
#     shuffled_deck = []
#     for card_index in range(len(left_part)):  # len(right_part)
#         shuffled_deck.append(left_part[card_index])
#         shuffled_deck.append(right_part[card_index])
#     deck_of_cards = shuffled_deck
# print(deck_of_cards)
#
# # 9
#
# collection_of_items = input().split("|")
# budget = float(input())
# ticket_price = 150
# money_for_shopping = 0
# money_from_selling = 0
# selling_prices_list = []
# for item in collection_of_items:
#     current_item = item.split("->")
#     item_type = current_item[0]
#     current_item_price = float(current_item[1])
#     if budget < current_item_price:
#         continue
#         # We should not but this item
#     if (item_type == "Clothes" and current_item_price > 50.00) or \
#             (item_type == "Shoes" and current_item_price > 35.00) or \
#             (item_type == "Accessories" and current_item_price > 20.50):
#         continue
#     money_for_shopping += current_item_price
#     budget -= current_item_price
#     selling_price = current_item_price * 1.40
#     money_from_selling += selling_price
#     selling_prices_list.append(f"{selling_price:.2f}")
# print(" ".join(selling_prices_list))
# profit = money_from_selling - money_for_shopping
# print(f"Profit: {profit:.2f}")
# budget += money_from_selling
# if budget >= ticket_price:
#     print("Hello, France!")
# else:
#     print("Not enough money.")
#
# # 10
#
# events = input().split("|")
# current_energy = 100
# current_coins = 100
# bakery_is_open = True
# for event in events:
#     event_items = event.split("-")
#     type_of_event = event_items[0]
#     event_value = int(event_items[1])
#     if type_of_event == "rest":
#         initial_energy = current_energy
#         current_energy += event_value
#         if current_energy > 100:
#             current_energy = 100
#         gained_energy = current_energy - initial_energy
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {current_energy}.")
#     elif type_of_event == "order":
#         if current_energy >= 30:  # I can complete the order
#             current_energy -= 30
#             current_coins += event_value
#             print(f"You earned {event_value} coins.")
#         else:
#             current_energy += 50
#             print("You had to rest!")
#     else:
#         if current_coins >= event_value:
#             current_coins -= event_value
#             print(f"You bought {type_of_event}.")
#         else:
#             bakery_is_open = False
#             print(f"Closed! Cannot afford {type_of_event}.")
#             break
# if bakery_is_open:
#     print("Day completed!")
#     print(f"Coins: {current_coins}")
#     print(f"Energy: {current_energy}")
#
# Examples:
#
# my_list = [1, 2, 3, 4, 2, 2, 3, 4, 5, 1, 5, 6, 7, 8, 9]

# my_list.sort(reverse=True)
# print(my_list)

# my_list.pop()
# print(my_list)

# my_list.pop(5)
# print(my_list)

# index = 3
# element = "Inserted element"
# my_list.insert(index, element)
# print(my_list)

# number = my_list.index(2)
# # print(number)

# repetition = my_list.count(2)
# print(repetition)

# my_list.reverse()
# print(my_list)

# index = 3
# del my_list[index]
# # print(my_list)

# some_element = 2
# my_list.remove(some_element)
# print(my_list)

# for index in range(len(my_list)):
#     if my_list[index] == 2:
#         my_list.pop(index)

# for index in range(len(my_list)-1,-1,-1):
#     if my_list[index] == 2:
#         my_list.pop(index)


# print(my_list)
# my_list = my_list[::-1]
# print(my_list)

# my_list_1 = my_list
# my_list_2 = my_list.copy()
# print(my_list)
# my_list_1.remove(2)
# print(my_list_1)
# print(my_list)
# print(my_list)
# my_list_2.remove(2)
# print(my_list_2)
# print(my_list)

#8
fire_cells = input().split('#')
# water = int(input())
# effort = 0
# total_fire_cells = 0
# cells_fire = []
# water_left = 0
# enough_water = 0
#
# print("Cells:")
#
# for index in range(len(fire_cells)):
#     cell = fire_cells[index].split()
#
#     if cell[0] == 'High':
#         if 81 <= int(cell[2]) <= 125:
#             enough_water = water - int(cell[2])
#             if water < enough_water:
#                 enough_water = 0
#                 continue
#             else:
#                 effort += int(cell[2]) * 0.25
#                 water_left += int(cell[2])
#                 cells_fire.append(cell[2])
#                 total_fire_cells += int(cell[2])
#
#         else:
#             water_left = 0
#
#     elif cell[0] == 'Medium':
#         if 51 <= int(cell[2]) <= 80:
#
#             enough_water += int(cell[2])
#             if water > enough_water:
#                 enough_water = 0
#                 continue
#             else:
#                 effort += int(cell[2]) * 0.25
#                 water_left += int(cell[2])
#                 cells_fire.append(cell[2])
#                 total_fire_cells += int(cell[2])
#
#         else:
#             water_left = 0
#
#     elif cell[0] == 'Low':
#         if 1 <= int(cell[2]) <= 50:
#             enough_water = water - int(cell[2])
#             if water < enough_water:
#                 enough_water = 0
#                 continue
#             else:
#                 effort += int(cell[2]) * 0.25
#                 water_left += int(cell[2])
#                 cells_fire.append(cell[2])
#                 total_fire_cells += int(cell[2])
#
#         else:
#             water_left = 0
#
# for cells in cells_fire:
#     print(f' - {cells}')
#
# print(f'Effort: {effort:.2f}')
# print(f"Total Fire: {total_fire_cells}")