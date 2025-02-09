first_list = input().split(', ')
second_list = input().split(', ')
new_list = []

for item in first_list:
    for item_ in second_list:
        if item in item_:
            new_list.append(item)
            break


print(new_list)