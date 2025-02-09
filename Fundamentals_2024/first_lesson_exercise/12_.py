quantity_of_decoration = int(input())
remaining_days = int(input())
total_cost = 0
total_spirit = 0
ornament_set_price = 2
tree_garland = 5

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decoration += 2
    if current_day % 2 == 0:
        total_cost += quantity_of_decoration * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0:
     total_spirit += 10 + 3
        #it not finished
    if current_day % 5 == 0:
        #its not finished
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        # you boy one item of sjirt, garlabd, lights and you don have spirit
if remaining_days % 10 == 0:
    total_spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')