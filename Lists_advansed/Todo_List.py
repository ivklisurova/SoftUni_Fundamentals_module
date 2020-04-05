todo_list = []

while True:
    todo_note = input().split('-')
    if todo_note[0] == 'End':
        break
    else:
        priority = int(todo_note[0])
        text = (todo_note[1])
        todo_list.append([priority, text])

x = len(todo_list)

result = x * [None]

for todo in todo_list:
    priority = todo[0]
    text = todo[1]
    result.insert(priority, text)

print([n for n in result if n])
