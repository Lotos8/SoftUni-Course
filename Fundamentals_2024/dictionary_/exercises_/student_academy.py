
length_of_grades = int(input())
students_data = {}
counter_list = []
for _ in range(length_of_grades):
    student = input()
    grades = float(input())

    if student not in students_data:
        count = 0
        students_data[student] = []

    students_data[student] += [grades]


for student in students_data:
    average_grade = 0
    numbers_of_grades = len(students_data[student])
    if numbers_of_grades > 1:
        grade_1 = students_data[student][0]
        grade_2 = students_data[student][1]
        average_grade = (grade_1 + grade_2) / numbers_of_grades

    else:
        average_grade = students_data[student][0]

    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")