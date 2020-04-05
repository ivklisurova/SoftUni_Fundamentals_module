first_row = input()
second_row = input()
third_row = input()

list_first_row = first_row.split()
list_second_row = second_row.split()
list_third_row = third_row.split()

matrix = [list_first_row, list_second_row, list_first_row]

winner = None

if list_first_row[0] == list_second_row[0] == list_third_row[0]:
    winner = list_first_row[0]
elif list_first_row[0] == list_first_row[1] == list_first_row[2]:
    winner = list_first_row[0]
elif list_first_row[0] == list_second_row[1] == list_third_row[2]:
    winner = list_first_row[0]
elif list_first_row[2] == list_second_row[1] == list_third_row[0]:
    winner = list_first_row[2]
elif list_second_row[0] == list_second_row[1] == list_second_row[2]:
    winner = list_second_row[0]
elif list_third_row[0] == list_third_row[1] == list_third_row[2]:
    winner = list_third_row[0]


if winner == '1':
    print('First player won')
elif winner == '2':
    print('Second player won')
else:
    print('Draw!')