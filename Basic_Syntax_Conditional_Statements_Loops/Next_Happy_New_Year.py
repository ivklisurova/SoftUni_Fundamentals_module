year = input()

int_next_happy_year = int(year) + 1

while True:
    next_happy_year = set(str(int_next_happy_year))

    if len(next_happy_year) == len(year):
        print(int_next_happy_year)
        break
    else:
        int_next_happy_year += 1
