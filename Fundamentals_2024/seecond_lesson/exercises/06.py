number_of_symbols = int(input())
for fist_symbol in range (97, 97 + number_of_symbols):
    for second_symbol in range(97, 97 + number_of_symbols):
        for third_symbol in range(97, 97 + number_of_symbols):
            print(f"{chr(fist_symbol)}{chr(second_symbol)}{chr(third_symbol)}")

