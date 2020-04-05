company_log = {}

while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' -> ')
    company = command[0]
    user = command[1]

    if company not in company_log:
        company_log[company] = []
    if user not in company_log[company]:
        company_log[company].append(user)

company_log = dict(sorted(company_log.items(), key=lambda x: x[0]))

for k, v in company_log.items():
    print(f'{k}')
    for i in v:
        print(f'-- {i}')
