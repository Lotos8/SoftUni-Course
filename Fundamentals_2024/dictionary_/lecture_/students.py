courses_dict = {}
students = []
course_to_search = ''
while True:
    students_info = input()

    if ':' not in students_info:
        course_to_search = students_info.lower()
        break

    name, id_, course = students_info.split(':')
    students.append({'name': name, 'id': id_, 'course': course})

for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['id']}")