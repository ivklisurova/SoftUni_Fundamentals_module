n = int(input())
p = int(input())

current_count_passengers = n
courses = 0

while current_count_passengers > 0:
    current_count_passengers -= p
    courses += 1

else:
    print(courses)
