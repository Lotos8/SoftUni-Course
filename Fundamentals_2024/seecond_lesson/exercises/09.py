number_of_snowball = int(input())


max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0
max_snowball_value = 0
for current_snowball in range(number_of_snowball):
    weight_of_snowball = int(input())
    time_of_snowball = int(input())
    quality_snowball = int(input())
    current_value = (weight_of_snowball // time_of_snowball) ** quality_snowball
    if current_value > max_snowball_value:
        max_snowball_weight = weight_of_snowball
        max_snowball_time = time_of_snowball
        max_snowball_quality = quality_snowball
        max_snowball_value = current_value
print(f"{max_snowball_weight} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})")