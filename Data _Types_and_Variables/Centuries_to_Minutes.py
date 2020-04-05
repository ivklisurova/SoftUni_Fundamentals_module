centuries = int(input())

YEARS = centuries * 100
DAYS = int(365.2422 * YEARS)
HOURS = DAYS * 24
MINUTES = HOURS * 60

print(f'{centuries} centuries = {YEARS} years = {DAYS} days = {HOURS} hours = {MINUTES} minutes')
