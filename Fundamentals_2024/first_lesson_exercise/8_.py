cups_of_coffee = 0
commend = input()
while commend != 'END':
    commend_ = commend

    if commend_ == 'cat' or commend_ == 'dog' or commend_ == 'coding' or commend_ == 'movie':
        cups_of_coffee += 1
    elif commend_ == 'CAT' or commend_ == 'DOG' or commend_ == 'CODING' or commend_ == 'MOVIE':
        cups_of_coffee += 2

    commend = input()
if cups_of_coffee <= 5:
    print(cups_of_coffee)
else:
    print('You need extra sleep')