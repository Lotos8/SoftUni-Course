
products = {}
while True:
    command = input()
    if " " not in command:
        break

    product, price, quantity = command.split()

    if product not in products:
        products[product] = {"price": 0, "value": 0}
        # products[product]= 0
    products[product]["price"] = float(price)
    products[product]["value"] += int(quantity)


for key in products.keys():
    total_price = products[key]["price"] * products[key]["value"]
    print(f"{key} -> {total_price:.2f}")