force_book = {}
while True:
    command = input()
    if ' | ' not in command or ' -> ' not in command:
        break

    if ' | ' in command:
        force_side, force_user = command.split(' | ')
        if force_side not in force_book:
            force_book[force_side] = ''
        force_user[force_side] += force_user

    elif ' -> ' in command:
        force_user, force_side  = command.split(' -> ')
        if force_user in force_book:
            pass
