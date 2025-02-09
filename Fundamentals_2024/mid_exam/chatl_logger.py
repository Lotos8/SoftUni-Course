list_massage = []
while True:
    chat = input().split()

    command = chat[0]

    if command == 'end':
        break

    if command == 'Chat':
        massage = chat[1]
        list_massage.append(massage)

    elif command == 'Delete':
        massage = chat[1]
        if massage in list_massage:
            list_massage.remove(massage)
    elif command == 'Edit':
        massage = chat[1]
        edited_version = chat[2]
        if massage in list_massage:
            index_unknow = list_massage.index(massage)
            list_massage[index_unknow] = edited_version
    elif command == 'Pin':
        massage = chat[1]
        if massage in list_massage:
            list_massage.remove(massage)
            list_massage.append(massage)

    elif command == 'Spam':
        chat.remove(chat[0])
        list_massage.extend(chat)


print('\n'.join(list_massage))

