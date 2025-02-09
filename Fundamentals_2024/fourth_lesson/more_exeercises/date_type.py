def result_of_data(types: str, data_given: any):
    if types == "string":
        return f"${data_given}$"
    elif types == "int":
        result = int(data_given) * 2
        return result
    elif types == "real":
        result = float(data_given) * 1.5
        return f"{result:.2f}"


type_of_data = input()
data = input()
print(result_of_data(type_of_data, data))