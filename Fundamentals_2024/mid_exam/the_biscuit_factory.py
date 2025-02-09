from math import floor

biscuits_made_form_person = int(input())
numbers_employs = int(input())
competing_factory_end_biscuits = int(input())
days_with_less_made_biscuits = 30 // 3
total_biscuits_per_day = biscuits_made_form_person * numbers_employs
total_biscuits = (total_biscuits_per_day * 20) + ((total_biscuits_per_day * days_with_less_made_biscuits) * 0.75)
dif_between_companies = abs(total_biscuits - competing_factory_end_biscuits)
percents_dif = dif_between_companies / competing_factory_end_biscuits * 100


print(f"You have produced {floor(total_biscuits)} biscuits for the past month.")
if competing_factory_end_biscuits <= total_biscuits:
    print(f"You produce {percents_dif:.2f} percent more biscuits.")
else:
    print(f"You produce {percents_dif:.2f} percent less biscuits.")

