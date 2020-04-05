import math

party_size = int(input())
days = int(input())

profit = 0
spent = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5

    profit += 50
    spent += 2 * party_size

    if day % 3 == 0:
        spent += 3 * party_size
    if day % 5 == 0:
        profit += party_size * 20
        if day % 3 == 0:
            spent += party_size * 2

total = profit - spent
coins_per_person = math.floor(total/party_size)
print(f"{party_size} companions received {coins_per_person} coins each.")
