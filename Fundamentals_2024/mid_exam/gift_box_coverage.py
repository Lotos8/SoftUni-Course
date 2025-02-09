size_of_side = float(input())
number_sheets_paper = int(input())
total_sheet = 0
gift_box = size_of_side * size_of_side * 6

for sheet in range(1, number_sheets_paper + 1):

    length_single_sheet = float(input())
    width_single_sheet = float(input())
    if sheet % 5 == 0:
        continue
    if sheet % 3 == 0:
        total_sheet += length_single_sheet * width_single_sheet * 0.75

    else:
        total_sheet += length_single_sheet * width_single_sheet


if total_sheet < gift_box:
    sheet_needed = ((gift_box - total_sheet) / gift_box) * 100
    print('You are out of paper!')
    print(f"{sheet_needed:.2f}% of the box is not covered.")

else:
    sheet_peper_left = ((total_sheet - gift_box)/total_sheet) * 100
    print('You\'ve covered the gift box!')
    print(f"{sheet_peper_left:.2f}% wrap paper left.")