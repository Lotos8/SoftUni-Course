n = int(input())
special_word = input()

string = []

for _ in range(n):
    current_string = input()
    string.append(current_string)

filtering_string = []

for current_string in string:
    if special_word in current_string:
        filtering_string.append(current_string)
        
print(string)
print(filtering_string)