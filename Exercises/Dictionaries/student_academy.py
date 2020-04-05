students_log = {}
above_average = {}

n = int(input())

for i in range(n):
    name = input()
    grade = float(input())
    if name not in students_log:
        students_log[name] = []
    students_log[name].append(grade)

for k, v in students_log.items():
    average = sum(v) / len(v)
    if average >= 4.50:
        above_average[k] = average

above_average = dict(sorted(above_average.items(), key=lambda x: x[1], reverse=True))

[print(f'{k} -> {v:.2f}') for k, v in above_average.items()]
