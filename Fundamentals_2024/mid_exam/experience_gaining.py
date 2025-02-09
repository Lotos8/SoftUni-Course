amount_of_experience = float(input())
count_of_battles = int(input())
experience = 0
number_of_battles = 0
#gets 15% more experience for every third battle
# and 10% less for every fifth battle,
# and 5% more experience on every fifteenth.
# You also need to stop the program as soon as he collects
# the needed experience.
for battle in range(1, count_of_battles + 1):
    gain_experience = float(input())

    number_of_battles += 1
    if battle % 3 == 0:
        gain_experience += gain_experience * 0.15
    if battle % 5 == 0:
        gain_experience -= gain_experience * 0.1
    if battle % 15 ==0:
        gain_experience += gain_experience * 0.05

    experience += gain_experience

    if amount_of_experience <= experience:
        break
if experience >= amount_of_experience:
    print(f"Player successfully collected his needed experience for {number_of_battles} battles.")
else:
    needed_experience = amount_of_experience - experience
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")