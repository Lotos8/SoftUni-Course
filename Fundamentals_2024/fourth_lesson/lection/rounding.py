def rounding(number: list):
    for n in number:
        new_number_list.append(round(n))
    return new_number_list


new_number_list = []
numbers_of_list = [float(num) for num in input().split()]
print(rounding(numbers_of_list))
