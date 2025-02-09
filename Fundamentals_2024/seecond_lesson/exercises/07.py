tank_capacity = 255
numbers_of_lines = int(input())
for line in range(numbers_of_lines):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0:
        print('Insufficient capacity!')
        continue
    tank_capacity -= liters_of_water
print(255 - tank_capacity)