def build_list(num1, num2, num3):
    ll_numbers = [num1, num2, num3]
    return ll_numbers


def solve(ll):
    negative_counter = 0
    if '0' in ll:
        return 'zero'
    for i in ll:
        if int(i) < 1:
            negative_counter += 1
    if negative_counter % 2 != 0:
        return 'negative'
    else:
        return 'positive'


num_1 = input()
num_2 = input()
num_3 = input()

print(solve(build_list(num_1, num_2, num_3)))
