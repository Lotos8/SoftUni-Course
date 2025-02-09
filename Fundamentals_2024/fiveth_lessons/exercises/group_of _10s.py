
numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers: # while len(numbers) > 0
    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    current_group += 10




