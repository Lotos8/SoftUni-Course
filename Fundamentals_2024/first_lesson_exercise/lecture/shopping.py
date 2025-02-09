budget = int(input())
amount = 0

while True:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
        
    price = int(command)
    amount += price

    if amount > budget:
        print('You went in overdraft!')
        break