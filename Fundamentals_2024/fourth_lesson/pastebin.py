# 1.1

first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []
for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)

# 1.2
first_sequence = input().split(", ")
second_sequence = input().split(", ")
print([first_string for first_string in first_sequence if
       any(first_string in second_string for second_string in second_sequence)])

# 2.1
version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
print(".".join(str(digit) for digit in version))

# 2.2
version = input().split(".")
version_as_integer = int("".join(version))
next_version = version_as_integer + 1
next_version_as_list = [s for s in str(next_version)]
print(".".join(next_version_as_list))

# 3

words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_words))

# 4.1

numbers = input().split(", ")
positive_numbers = ", ".join([number for number in numbers if int(number) >= 0])
negative_numbers = ", ".join([number for number in numbers if int(number) < 0])
even_numbers = ", ".join([number for number in numbers if int(number) % 2 == 0])
odd_numbers = ", ".join([number for number in numbers if int(number) % 2 != 0])
print(f"Positive: {positive_numbers}")
print(f"Negative: {negative_numbers}")
print(f"Even: {even_numbers}")
print(f"Odd: {odd_numbers}")


# 4.2

def positive_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if int(number) >= 0])


def negative_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if int(number) < 0])


def even_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if int(number) % 2 == 0])


def odd_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if int(number) % 2 != 0])


numbers = input().split(", ")
print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")

# 5
count_of_rooms = int(input())
total_free_chairs = 0
for number_of_room in range(1, count_of_rooms + 1):
    free_chairs_in_this_room, visitors = input().split()
    difference = len(free_chairs_in_this_room) - int(visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {number_of_room}")
    total_free_chairs += difference
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

# 6
number_of_electrons = int(input())
shells = []
for shell in range(1, number_of_electrons + 1):
    max_electrons_in_current_shell = 2 * shell ** 2
    if number_of_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
        number_of_electrons -= max_electrons_in_current_shell
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break
print(shells)

# 7
numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:  # while len(numbers) > 0
    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    current_group += 10


# 11


def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons, title, index_of_inserting):
    if title not in list_of_lessons:
        list_of_lessons.insert(index_of_inserting, title)
    return list_of_lessons


def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        title_index = list_of_lessons.index(title)
        if title_index + 1 in range(len(list_of_lessons)):
            if "Exercise" in list_of_lessons[title_index + 1]:  # if list_of_lessons[title_index +1] == f"Exercise":
                list_of_lessons.pop(title_index + 1)
        list_of_lessons.remove(title)
    return list_of_lessons


def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        first_lesson_has_exercise = False
        second_lesson_has_exercise = False
        if first_position + 1 in range(len(list_of_lessons)):
            first_lesson_has_exercise = "Exercise" in list_of_lessons[first_position + 1]
        if second_position + 1 in range(len(list_of_lessons)):
            second_lesson_has_exercise = "Exercise" in list_of_lessons[second_position + 1]
        # Swap lessons
        list_of_lessons[first_position], list_of_lessons[second_position] = list_of_lessons[second_position], \
                                                                            list_of_lessons[first_position]
        # Swap exercises
        if first_lesson_has_exercise and second_lesson_has_exercise:
            list_of_lessons[first_position + 1], list_of_lessons[second_position + 1] = \
                list_of_lessons[second_position + 1], list_of_lessons[first_position + 1]
        elif not first_lesson_has_exercise and second_lesson_has_exercise:
            # list_of_lessons.insert(first_position + 1, list_of_lessons[second_position + 1])
            # list_of_lessons.pop(second_position + 1)
            list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))
        elif first_lesson_has_exercise and not second_lesson_has_exercise:
            # list_of_lessons.insert(second_position +1, list_of_lessons[first_position + 1])
            # list_of_lessons.pop(first_position + 1)
            list_of_lessons.insert(second_position + 1, list_of_lessons.pop(first_position + 1))
    return list_of_lessons


def exercise(list_of_lessons, title):
    exercise_name = f"{title}-Exercise"
    if title in list_of_lessons and exercise_name not in list_of_lessons:
        lesson_index = list_of_lessons.index(title)
        list_of_lessons.insert(lesson_index + 1, exercise_name)
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(exercise_name)
    return list_of_lessons


lessons = input().split(", ")
command = input().split(":")
while len(command) > 1:
    action = command[0]
    lesson_title = command[1]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        index = int(command[2])
        lessons = insert_lesson(lessons, lesson_title, index)
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        next_lesson_title = command[2]
        lessons = swap_lesson(lessons, lesson_title, next_lesson_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input().split(":")
for index, lesson_or_exercise in enumerate(lessons):
    print(f"{index + 1}.{lesson_or_exercise}")