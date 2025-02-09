to_do_list = []
task = input()
new_to_do_list = []
while task != 'End':
    to_do_list.append(task)
    task = input()
for remove_elements in sorted(to_do_list):
    elements = remove_elements.split('-')
    new_to_do_list.append(elements[1])
print(new_to_do_list)

# notes = [0] * 10
# while True:
#  command = input()
#  if command == "End":
#  break
#  tokens = command.split("-")
#  priority = int(tokens[0]) - 1
#  note = tokens[1]
#  notes.pop(priority)
#  notes.insert(priority, note)
