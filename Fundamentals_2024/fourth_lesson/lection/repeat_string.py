string = input()
number_of_repetitions = int(input())

new_string = lambda word, number: word * number
print(new_string(string, number_of_repetitions))
