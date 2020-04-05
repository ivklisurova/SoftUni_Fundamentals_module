population = input().split(',')
minimum_wealth = int(input())

population = [int(i) for i in population]


for i, j in enumerate(population):
    if j < minimum_wealth:
        diff = minimum_wealth - j
        max_wealth = max(enumerate(population))
        if max_wealth[1] > minimum_wealth and (max_wealth[1] - diff) >= minimum_wealth:
            population[max_wealth[0]] = max_wealth[1] - diff
            population[i] = j + diff

if not all(i >= minimum_wealth for i in population):
    print('No equal distribution possible')
else:
    print(population)