initial_energy = 100
initial_coins = 100

working_day_events = input().split("|")
is_completed = True

for event in working_day_events:
    token = event.split("-")
    action = token[0]
    if action == "rest":
        if initial_energy + int(token[1]) <= 100:
            initial_energy += int(token[1])
            print(f"You gained {int(token[1])} energy.")
        else:
            diff = 100 - initial_energy
            initial_energy += diff
            print(f"You gained {diff} energy.")
        print(f"Current energy: {initial_energy}.")
    elif action == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += int(token[1])
            print(f"You earned {int(token[1])} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins > int(token[1]):
            initial_coins -= int(token[1])
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            is_completed = False
            break
if is_completed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
