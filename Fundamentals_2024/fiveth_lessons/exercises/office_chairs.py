rooms = int(input())
total_free_chairs = 0
for room in range(1, rooms + 1):
    free_chairs, visitors = input().split()
    difference = len(free_chairs) - int(visitors)
    total_free_chairs += difference
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room}")

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")