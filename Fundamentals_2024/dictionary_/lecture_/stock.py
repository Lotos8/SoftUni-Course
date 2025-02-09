stock_list = input().split(' ')
stock_dict = {stock_list[i]: stock_list[i +1] for i in range(0, len(stock_list), 2)}
search_product = input().split(' ')

for product in search_product:
    if product in stock_dict:
        print(f"We have {stock_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")




