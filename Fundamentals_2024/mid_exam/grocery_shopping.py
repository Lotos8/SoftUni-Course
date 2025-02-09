list_products = [i for i in input().split('|')]

while True:
    commands = input().split('%')

    if commands[0] == 'Shop!':
        break

    if commands[0] == 'Important':
        product_ = commands[1]
        if product_ in list_products:
            index = list_products.index(product_)
            list_products.remove(product_)
            list_products.insert(0,product_)

        else:
            list_products.insert(0,product_)

    elif commands[0] == 'Add':
        product_ = commands[1]
        if product_ in list_products:
            print("The product is already in the list.")
        else:
            list_products.append(product_)
    elif commands[0] == 'Swap':
        product_ = commands[1]
        product_2 = commands[2]
        if product_ in list_products and product_2 not in list_products:
            print(f"Product {product_2} missing!")
        elif product_2 in list_products and product_ not in list_products:
            print(f"Product {product_} missing!")
        else:
            index_1 = list_products.index(product_)
            index_2 = list_products.index(product_2)
            list_products[index_1], list_products[index_2] = list_products[index_2], list_products[index_1]
    elif commands[0] == 'Remove':
        product_ = commands[1]
        if product_ in list_products:
            list_products.remove(product_)
        else:
            print(f"Product {product_} isn't in the list.")
    elif commands[0] == 'Reversed':
        list_products.reverse()

num = 0
for add_num_product in list_products:
    num += 1
    print(f"{num}. {add_num_product}")