
day_of_adventures = int(input())
count_of_the_participants = int(input())
initial_energy = float(input())
water_per_person = float(input())
food_per_person = float(input())
days_counter = 0

total_water_for_all = count_of_the_participants * water_per_person * day_of_adventures
total_food_for_all = count_of_the_participants * food_per_person * day_of_adventures

for day in range(1, day_of_adventures + 1):
    energy_loss = float(input())
    days_counter += 1
    initial_energy -= energy_loss
    if initial_energy <= 0:
        print(f'You will run out of energy. You will be left with {total_food_for_all:.2f} food and {total_water_for_all:.2f} water.')
        break
    if days_counter % 2 == 0:
        initial_energy += initial_energy * 0.05
        total_water_for_all -= total_water_for_all * 0.30
    elif days_counter % 3 == 0:
        initial_energy += initial_energy * 0.10
        total_food_for_all -= total_food_for_all / count_of_the_participants

if initial_energy > 0:
    print(f"You are ready for the quest. You will be left with {initial_energy:.2f} energy!")
