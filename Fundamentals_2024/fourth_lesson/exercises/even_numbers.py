list_of_string = input().split()
list_of_number = []

for number in list_of_string:
    list_of_number.append(int(number))

even_number = lambda x: x % 2 == 0
list_of_even_numbers = list(filter(even_number, list_of_number))
print(list_of_even_numbers)