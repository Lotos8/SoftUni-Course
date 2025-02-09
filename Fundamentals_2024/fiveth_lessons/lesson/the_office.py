list_of_happiness = list(map(int, input().split()))
improvement_factor = int(input())
total_count = len(list_of_happiness)

improved_happiness = [score * improvement_factor for score in list_of_happiness]

average_improvement = sum(improved_happiness) / total_count
happy_count = len([num for num in improved_happiness if num >= average_improvement])

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")