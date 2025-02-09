def calculator(func_parameter: str, first_num: int, second_num: int)-> int:
    if func_parameter == "add":
        return first_num + second_num
    elif func_parameter == "subtract":
        return first_num - second_num
    elif func_parameter == "multiply":
        return first_num * second_num
    elif func_parameter == "divide":
        return int(first_num / second_num)


parameter = input()
first_number = int(input())
second_number = int(input())
print(calculator(parameter, first_number, second_number))
