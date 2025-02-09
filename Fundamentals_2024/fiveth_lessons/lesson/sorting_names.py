name_list = input().split(', ')
new_list = sorted(name_list, key=lambda x: (-len(x), x))

print(new_list)