budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = (price_flour + (price_flour * 0.25)) / 4

price_cozonac = price_flour + price_eggs + price_milk

cozonac_counter = 0
eggs_counter = 0

while True:
    if budget < price_cozonac:
        break
    budget -= price_cozonac
    cozonac_counter += 1
    eggs_counter += 3
    if cozonac_counter % 3 == 0:
        eggs_counter -= (cozonac_counter - 2)

print(f'You made {cozonac_counter} cozonacs! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.')
