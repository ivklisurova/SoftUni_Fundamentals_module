n_integer = input()

list_integers = n_integer.split(', ')

for i in list_integers:
    if i == '0':
        list_integers.remove('0')
        list_integers.append('0')

new_list = list(map(int,list_integers))
print(new_list)
