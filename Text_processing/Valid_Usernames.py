user_names = input().split(', ')

valid_user_names = []

for user in user_names:
    if 3 <= len(user) <= 16 and (user.isalnum() or '-' in user or '_' in user):
        print(user)
