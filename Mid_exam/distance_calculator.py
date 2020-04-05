steps_made = int(input())
step_length = float(input())
required_distance = int(input()) * 100

distance_traveled = 0

for step in range(1, steps_made + 1):
    if step % 5 == 0:
        distance_traveled += step_length * 0.7
    else:
        distance_traveled += step_length

percentage = distance_traveled/required_distance * 100

print(f'You travelled {percentage:.2f}% of the distance!')
