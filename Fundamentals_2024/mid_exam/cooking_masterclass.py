from math import ceil
budget = float(input())
students = int(input())
package_flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

numbers_of_aprons = ceil(students + (students * 0.2))
numbers_of_flour_package = students - (students // 5)

total_price_flour = numbers_of_flour_package * package_flour_price
total_price_eggs = egg_price * 10 * students
total_price_apron = numbers_of_aprons * apron_price

total_expenses = total_price_flour + total_price_eggs + total_price_apron

differ = abs(total_expenses - budget)

if budget >= total_expenses:
    print(f"Items purchased for {total_expenses:.2f}$.")
else:
    print(f"{differ:.2f}$ more needed.")