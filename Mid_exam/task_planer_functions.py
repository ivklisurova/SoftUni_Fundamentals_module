def actions(string, ll, new_value):
    tokens = string.split()
    idx = int(tokens[1])

    is_valid = False

    if len(ll) > idx >= 0:
        is_valid = True

    if is_valid:
        ll[idx] = new_value
        return ll


def count(string, ll):
    tokens = string.split()
    action = tokens[1]
    if action == 'Completed':
        print(ll.count(0))
    elif action == 'Incomplete':
        incomplete_tasks = [i for i in ll if i > 0]
        print(len(incomplete_tasks))
    elif action == 'Dropped':
        print(ll.count(-1))


def output(ll):
    [print(x, end=' ') for x in ll if x > 0]


tasks = list(map(int, input().split()))

while True:
    command = input()
    if command == 'End':
        break
    if command.startswith('Complete'):
        actions(command, tasks, 0)
    elif command.startswith('Change'):
        new_value = command.split()[2]
        actions(command, tasks, int(new_value))
    elif command.startswith('Drop'):
        actions(command, tasks, -1)
    elif command.startswith('Count'):
        count(command, tasks)

output(tasks)
