def solve(a, b, ll):
    if a <= b:
        ll.append(a)
    elif a > b:
        ll.append(b)
    return ll


free_electrons = int(input())

shell = []
shell_counter = 1

while True:
    if free_electrons <= 0:
        break
    electrons = 2 * shell_counter ** 2
    solve(electrons, free_electrons, shell)
    free_electrons -= electrons

    shell_counter += 1

print(shell)
