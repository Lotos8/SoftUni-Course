list_of_secret_words = [word for word in input().split()]
new_secret_words = []
character = []
for secret_word in list_of_secret_words:
    for char in secret_word:
        if char.isalpha():
            new_secret_words.append(char)
        if int(char) > 0:
            character.append(''.join(char))
    letter = chr(int, character)



    print(character)
