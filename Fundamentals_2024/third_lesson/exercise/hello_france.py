#train ticket costs exactly 150$.
#sell them at a higher price – with a 40% markup
list_with_items = [container for container in input().split('|')]
budget = float(input())
ticket_price = 150
list_prices = []
total_price = 0
money = 0
current_budget = budget
left_money = 0
sold_items = 0
for split_items_and_price in range(len(list_with_items)):

    item_price = list_with_items[split_items_and_price].split('->')
    item = item_price[0]
    price = float(item_price[1])

    if item == 'Clothes':
        if price > 50.00:
            continue
    elif item == 'Shoes':
        if price > 35.00:
            continue
    elif item == 'Accessories':
        if price > 20.50:
            continue

    current_budget -= price
    if current_budget < 0:
        break
    increased_price = price * 0.40
    selling_price = price + increased_price
    sold_items += selling_price
    list_prices.append(f"{selling_price:.2f}")
    total_price += selling_price
    left_money = current_budget
convert = ' '.join(map(str, list_prices))
print(f"{convert}")
left_money += sold_items
profit = abs(left_money - budget)
print(f'Profit: {profit:.2f}')
if left_money >= ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')







