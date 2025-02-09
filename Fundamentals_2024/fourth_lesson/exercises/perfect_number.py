
def perfect_number(num):
    sum_number = 0
    for n in range(1, num):
        if num % n == 0:
            sum_number += n
    return sum_number == num


number = int(input())
is_perfect = perfect_number(number)
if not is_perfect:
    print("It's not so perfect.")
else:
    print("We have a perfect number!")
