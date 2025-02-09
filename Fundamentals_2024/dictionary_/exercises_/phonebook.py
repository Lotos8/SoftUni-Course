def convert(lst, dict_):
    for i in range(0, len(lst), 2):
        dict_[lst[i]] = lst[i + 1]
    return dict_


phonebook_dict = {}
phonebook_list = []
counter_of_people = 0

while True:
    contact = input()

    if '-' not in contact:
        counter_of_people = int(contact)
        break

    contact_name, number = contact.split('-')
    phonebook_list.append(contact_name)
    phonebook_list.append(number)


for number_of_people in range(counter_of_people):
    names = input()
    dict_of_contacts = convert(phonebook_list,phonebook_dict)
    if names in dict_of_contacts.keys():
        print(f"{names} -> {dict_of_contacts[names]}")
    else:
        print(f"Contact {names} does not exist.")

