string = input().lower()

count_of_sand = string.count('sand', 0, len(string))
count_of_water = string.count('water', 0, len(string))
count_of_fish = string.count('fish', 0, len(string))
count_of_sun = string.count('sun', 0, len(string))

count_of_words = count_of_sand+count_of_water+count_of_fish+count_of_sun

print(count_of_words)
