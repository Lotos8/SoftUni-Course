list_numbers = input().split()
count_of_number_to_remove = int(input())
current_list_of_numbers = []
for n in range(len(list_numbers)):
    current_list_of_numbers.append(int(list_numbers[n]))
for i in range(count_of_number_to_remove):
    current_list_of_numbers.remove(min(current_list_of_numbers))

convert = ', '.join(map(str, current_list_of_numbers))
print(convert)

