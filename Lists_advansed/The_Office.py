import math

employee_happiness = list(map(lambda x: int(x), input().split()))
happiness_improvement_factor = int(input())
total_count = len(employee_happiness)

multiplied_happiness = [x * happiness_improvement_factor for x in employee_happiness]

average = math.floor(sum(multiplied_happiness) / len(multiplied_happiness))

filtered_list = [x for x in multiplied_happiness if x > average]
happy_count = len(filtered_list)


if happy_count >= total_count//2:
    print(f'Score: {happy_count}/{total_count}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{total_count}. Employees are not happy!')





