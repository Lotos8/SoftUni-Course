def string(option):
    sentence = "Learning Python is fun!"
    first_part_of_sentences = sentence[0:8]
    second_part_of_sentences = sentence[16:23]
    all_parts_together = first_part_of_sentences + ' ' + second_part_of_sentences
    uppercase_string = all_parts_together.upper()
    replacement_string = uppercase_string.replace("FUN", "AWESOME")
    return replacement_string


def number(num1, num2):
    list_with_results = []
    add_result = f"Result: {int(num1) + int(num2)}"
    list_with_results.append(add_result)
    sub_result = f"Result: {int(num1) - int(num2)}"
    list_with_results.append(sub_result)
    mul_result = f"Result: {int(num1) * int(num2)}"
    list_with_results.append(mul_result)

    if float(num2) == 0:
        error = "Error: Division by zero is not allowed."
        list_with_results.append(error)
    else:
        div_result = f"Result: {int(num1) / int(num2)}"
        list_with_results.append(div_result)

    power_result = f"Result: {int(num1) ** int(num2)}"
    list_with_results.append(power_result)

    return list_with_results


def boolean():
    pass


def additional_data_types():
    pass


print("Choose from the following:\n"
      "1. Strings\n"
      "2. Numbers\n"
      "3. Booleans\n"
      "4. Additional Data Types (List, Tuple, Dictionary)\n")

choice = input("Give your choice: ")

if choice == "1":
    print(string(choice))
elif choice == "2":
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")
    print(number(number1, number2))
elif choice == "3":
    print(boolean())
elif choice == "4":
    print(additional_data_types())
