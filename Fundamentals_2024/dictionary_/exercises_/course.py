courses_data = {}
courses_counter = 0
while True:
    data = input()

    if ' : ' not in data:
        break

    course, name = data.split(' : ')

    if course not in courses_data:
        courses_data[course] = []
    courses_data[course] += [name]


for course, names in courses_data.items():
    number_of_students = courses_data[course]
    students = len(number_of_students)
    print(f"{course}: {students}")
    for name in courses_data[course]:
        print(f"-- {name}")
