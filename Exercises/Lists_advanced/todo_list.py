def append(ll):
    priority = int(todo_note[0])
    text = (todo_note[1])
    ll.append([priority, text])
    return ll


todo_list = []

while True:
    todo_note = input().split('-')
    if todo_note[0] == 'End':
        break
    else:
        append(todo_list)

priority_list = list(sorted(todo_list, key=lambda x: x[0]))

print([i[1] for i in priority_list])
