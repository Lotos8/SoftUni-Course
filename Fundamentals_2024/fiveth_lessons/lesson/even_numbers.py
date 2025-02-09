numbers_list = list(map(int, input().split(', ')))

# even_number = list(filter(lambda x: x % 2 == 0, numbers_list))
even_indices = [index for index, num in enumerate(numbers_list) if num % 2 == 0]
# list_of_index = []
# for number in even_number:
#     index = numbers_list.index(int(number))
#     list_of_index.append(index)

print(even_indices)