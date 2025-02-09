car_list_for_taxes = input().split('>>')

total_tax_car = 0
total_tax = 0
for cars in range(len(car_list_for_taxes)):
    date_car = car_list_for_taxes[cars].split()

    car = date_car[0]
    years = int(date_car[1])
    car_kilometers = int(date_car[2])
    if car == 'family':
        over_3000_km = car_kilometers // 3000
        if over_3000_km >= 1:
            total_tax_car = (50 - (years * 5)) + over_3000_km * 12
            total_tax += total_tax_car
        print(f"A {car} car will pay {total_tax_car:.2f} euros in taxes.")
    elif car == 'heavyDuty':
        over_9000_km = car_kilometers // 9000
        if over_9000_km >= 1:
            total_tax_car = (80 - (years * 8)) + over_9000_km * 14
            total_tax += total_tax_car
        print(f"A {car} car will pay {total_tax_car:.2f} euros in taxes.")
    elif car == 'sports':
        over_2000_km = car_kilometers // 2000
        if over_2000_km >= 1:
            total_tax_car = (100 - (years * 9)) + over_2000_km * 18
            total_tax += total_tax_car
        print(f"A {car} car will pay {total_tax_car:.2f} euros in taxes.")
    else:
        print("Invalid car type." )


print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes." )