command = input()

activities = ['coding', 'dog', 'cat', 'movie', 'CODING', 'DOG', 'CAT', 'MOVIE', 'Dog', 'Coding', 'Movie', 'Cat']

coffee_counter = 0

while command != 'END':
    if command in activities:
        if command.isupper():
            coffee_counter += 2
        elif command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 1

    command = input()
else:
    if coffee_counter > 5:
        print('You need extra sleep')
    else:
        print(coffee_counter)
