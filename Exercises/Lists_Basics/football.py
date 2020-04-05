a = b = 11
c = []
comm = input().split(" ")

for i in comm:
    if i not in c:
        c.append(i)
        if i[0] == "A":
            a -= 1
        if i[0] == "B":
            b -= 1

print(f"Team A - {a}; Team B - {b}")

if a < 7 or b < 7:
    print("Game was terminated")