def print_progress_bar(percentage):
    percent_symbols = percentage // number_of_symbols
    point_symbols = number_of_symbols - percent_symbols
    return f"{percentage}% [{'%' * percent_symbols}{'.' * point_symbols}]\nStill loading..."


number = int(input())
number_of_symbols = 10
if number == 100:
    print(f"{number}% Complete!")
    print("[%%%%%%%%%%]")
else:
    print(print_progress_bar(number))
