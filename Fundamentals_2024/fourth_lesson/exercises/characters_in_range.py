def symbols_of_ascii_table(symbol1, symbol2):
    for n in range(ord(symbol1) + 1, ord(symbol2)):
        list_of_symbols.append(' '.join(chr(n)))
    return list_of_symbols


list_of_symbols = []
first_symbol = input()
second_symbol = input()
result = symbols_of_ascii_table(first_symbol, second_symbol)
print(" ".join(result))
