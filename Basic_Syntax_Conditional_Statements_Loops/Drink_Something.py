age = int(input())

drink = None

if age <= 14:
    drink = 'toddy'
elif age > 14 and age <= 18:
    drink = 'coke'
elif age > 18 and age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f'drink {drink}')
