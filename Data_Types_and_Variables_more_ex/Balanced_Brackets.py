n = int(input())

is_balanced = False

previous_string = None

for i in range(n):
    string = input()

    if i == 0:
        previous_string = string
    if string == '(':
        if previous_string == ')':
            is_balanced = True
            previous_string = string
        else:
            is_balanced = False
    elif string == ')':
        if previous_string == '(':
            is_balanced = True
            previous_string = string
        else:
            is_balanced = False

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

