budget = float(input())
price_flour_kg = float(input())

pack_eggs = price_flour_kg * 0.75
price_milk_250 = (price_flour_kg * 1.25) / 4

price_for_cozonac = price_flour_kg + pack_eggs + price_milk_250
left_budget = budget

cozonac_count = 0
eggs_count = 0

while True:
    if left_budget >= price_for_cozonac:
        left_budget -= price_for_cozonac
        cozonac_count += 1
        eggs_count += 3
        if cozonac_count % 3 == 0:
            eggs_count -= cozonac_count -2

    else:
        print(f'You made {cozonac_count} cozonacs! Now you have {eggs_count} eggs and {left_budget:.2f}BGN left.')
        break
