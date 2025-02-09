product_dict = {}
while True:
    products = input()

    if ': ' not in products:
        break

    product, quantity = products.split(': ')
    if product not in product_dict:
        product_dict[product] = 0

    product_dict[product] += int(quantity)

print("Products in stock:")
for key, value in product_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(product_dict)}")
print(f"Total Quantity: {sum(product_dict.values())}")
