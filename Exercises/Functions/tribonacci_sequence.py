def solve(rep):
    ll = []
    for i in range(rep):
        if i == 0:
            ll.append(1)
        elif 0 < i <= 2:
            a = sum(ll)
            ll.append(a)
        else:
            num = ll[i - 1] + ll[i - 2] + ll[i - 3]
            ll.append(num)
    return ' '.join([str(x) for x in ll])


n = int(input())

print(solve(n))