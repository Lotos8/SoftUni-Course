number = float(input())

if number == 0:
    print('zero')
elif number < 1000000 and number >= 1:
    print('positive')
elif number > -100000 and number < -1:
    print('negative')
elif number < 1 and number > 0:
        print('small positive')
elif number > -1 and number < 0:
        print('small negative')
elif number > 1000000:
    print('large positive')
elif number < -1000000:
    print('large negative')
