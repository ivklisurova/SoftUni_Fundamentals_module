rooms = int(input())

free_chairs = []

for room in range(1,rooms+1):
    room_ocupacity = input().split()
    chairs = room_ocupacity[0]
    people_in_room = int(room_ocupacity[1])

    count_chairs = chairs.count('X')
    diff = abs(count_chairs - people_in_room)

    if count_chairs < people_in_room:
        print(f'{diff} more chairs needed in room {room}')
    else:
        free_chairs.append(diff)

if len(free_chairs) == rooms:
    total_free_chairs = sum(free_chairs)
    print(f'Game On, {total_free_chairs} free chairs left')
