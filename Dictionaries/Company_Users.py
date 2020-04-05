company_log = {}

while True:
    command = input()
    if command == 'End':
        break
    company, employee = command.split(' -> ')

    if company not in company_log:
        company_log[company] = []
        company_log[company].append(employee)
    else:
        if employee not in company_log[company]:
            company_log[company].append(employee)


company_log = dict(sorted(company_log.items()))

for k in company_log.keys():
    print(f'{k}')
    for v in company_log[k]:
        print(f'-- {v}')
