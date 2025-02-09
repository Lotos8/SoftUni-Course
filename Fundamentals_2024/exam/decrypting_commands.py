crypting_word = input()

while True:

    command = input().split()

    if command[0] == 'Finish':
        break

    if command[0] == 'Replace':
        current_char = command[1]
        new_char= command[2]
        if current_char in crypting_word:
            crypting_word = crypting_word.replace(current_char, new_char)
            print(crypting_word)
    elif command[0] == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 < start_index < len(crypting_word) and 0 < end_index < len(crypting_word):
            crypting_word = crypting_word[:start_index+ 1] + crypting_word[end_index+2:]
            print(crypting_word)
        else:
            print("Invalid indices!")

    elif command[0] == 'Make':
        upper_lower_cases = command[1]
        if upper_lower_cases == 'Upper':
            crypting_word = crypting_word.upper()
            print(crypting_word)
        elif upper_lower_cases == 'Lower':
            crypting_word = crypting_word.lower()
            print(crypting_word)


    elif command[0] == 'Check':
        text = command[1]
        if text in crypting_word:
            print(f"Message contains {text}")
        else:
            print(f"Message doesn't contain {text}")

    elif command[0] == 'Sum':
        start_index = int(command[1])
        end_index = int(command[2])
        sum_ascii_nums = 0
        if 0 < start_index < len(crypting_word) and 0 < end_index < len(crypting_word):
            substring = crypting_word[start_index:end_index+1]
            for char in substring:
                sum_ascii_nums += ord(char)
            print(sum_ascii_nums)
        else:
            print("Invalid indices!")