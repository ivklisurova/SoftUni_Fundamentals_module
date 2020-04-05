import math

students_count = int(input())
lectures = int(input())
initial_bonus = int(input())

max_bonus = 0
max_lectures = 0

for student in range(students_count):
    attendances = int(input())
    total_bonus = attendances / lectures * (5 + initial_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_lectures = attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {max_lectures} lectures.')
