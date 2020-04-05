tasks = list(map(int, input().split()))

while True:
    command = input()
    if command == 'End':
        break
    command = command.split()
    if command[0] == 'Complete':
        idx = int(command[1])
        if 0 <= idx < len(tasks):
            tasks[idx] = 0
    elif command[0] == 'Change':
        index = int(command[1])
        new_value = int(command[2])
        if 0 <= index < len(tasks):
            tasks[index] = new_value
    elif command[0] == 'Drop':
        indx = int(command[1])
        if 0 <= indx < len(tasks):
            tasks[indx] = -1
    elif command[0] == 'Count':
        if command[1] == 'Completed':
            print(tasks.count(0))
        elif command[1] == 'Incomplete':
            counter = len([i for i in tasks if i > 0])
            print(counter)
        elif command[1] == 'Dropped':
            print(tasks.count(-1))

for x in tasks:
    if x > 0:
        print(x, end=' ')
