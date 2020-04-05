contest_log = {}

while True:
    contest_input = input()
    if contest_input == 'end of contests':
        break
    tokens = contest_input.split(':')
    contest = tokens[0]
    password = tokens[1]

    if contest not in contest_log:
        contest_log[contest] = []
        contest_log[contest].append(password)

while True:
    contesters_input = input()
    if contesters_input == 'end of submissions':
        break
    tokens_contesters = contesters_input.split('=>')
    contest = tokens_contesters[0]
    password = tokens_contesters[1]
    username = tokens_contesters[2]
    points = tokens_contesters[3]
    if contest in contest_log:
        if password in contest_log[1]:
            if username not in contest:
                password[username] = {points}


                print(contest_log)












