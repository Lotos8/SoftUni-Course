#for i in range(1, 5 + 1):
#    for j in range(0, i):
#        print('*', end='')
#    print()


for row in range(1, 5 + 1):
    for col in range(0, row):
        if row == 2 or 3 or 4:
            if col == 2 or 3 or 4:
                print()
                print()
            else:
                print('*', end='')



