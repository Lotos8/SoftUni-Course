character_list = input().split(', ')
ascii_dictionary = {}

for char in character_list:
    ascii_dictionary[char] = ord(char)
print(ascii_dictionary)