def add_stop(stop: str, index_of_text: int, text: str):
    if index_of_text < len(stop):
        stop = stop[:index_of_text] + text + stop[index:]
    return stop

def remove_stop(stop: str, start_text: int, end_text: int):
    if start_text < len(stop) and end_text < len(stops):
        stop = stop[:start_text] + stop[end_text + 1:]
    return stop

def switch(stop: str, old_text: str, new_text):
    if old_text in stop:
        if switch:
            stop = stop.replace(old_string, new_string)
    return stop


stops = input()

while True:
    command = input().split(':')

    if command[0] == 'Travel':
        print('Ready for world tour! Planned stops:', end=' ')
        print(stops)
        break

    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        stops = add_stop(stops, index, string)

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        stops = remove_stop(stops, start_index, end_index)

    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        stops = switch(stops, old_string,new_string)
    print(stops)
