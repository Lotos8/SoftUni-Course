
number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield = number_of_lost_fights // (2 * 3)
total_armor = total_shield // 2
expenses = total_helmet_broken * helmet_price \
           + total_sword_broken * sword_price \
           + total_shield * shield_price \
           + total_armor * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")