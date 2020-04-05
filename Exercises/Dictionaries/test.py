username_and_results = {}
language_submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split('-')
    name = command[0]
    if command[1] == 'banned':
        username_and_results.pop(name)
    else:
        language = command[1]
        result = int(command[2])
        if name not in username_and_results:
            username_and_results[name] = result
        else:
            if username_and_results[name] < result:
                username_and_results[name] = result

        if language not in language_submissions:
            language_submissions[language] = 1
        else:
            language_submissions[language] += 1

print("Results:")
for user, score in sorted(username_and_results.items(), key=lambda x: (-x[1], x[0])):
    print(f"{user} | {score}")

print("Submissions:")
for language, score in sorted(language_submissions.items(), key=lambda x: (-x[1], x[0])):
    print(f"{language} - {score}")