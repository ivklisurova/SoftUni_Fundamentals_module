n = int(input())

students_log = {}

for i in range(0,n):
    name = input()
    grade = float(input())

    if name not in students_log:
        students_log[name] = []
        students_log[name].append(grade)
    else:
        students_log[name].append(grade)

students_log = dict(sorted(students_log.items(),key=lambda x:(sum(x[1])/len(x[1])),reverse=True))

[print(f'{k} -> {sum(v)/len(v):.2f}') for k,v in students_log.items() if (sum(v)/len(v)) >= 4.5]

# for k,v in students_log.items():
#     average = sum(v)/len(v)
#     if average >= 4.5:
#         print(f'{k} -> {average:.2f}')