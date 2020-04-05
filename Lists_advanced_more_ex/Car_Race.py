input_string = input().split()

middle_el = (int(len(input_string) // 2))

left = input_string[:middle_el]
right = list(reversed(input_string[middle_el:]))


def score(string):
    result = 0
    for i in string:
        result += int(i)
        if int(i) == 0:
            result *= 0.8
    return result


first_car_score = ['left', score(left)]
second_car_score = ['right', score(right)]

winner = min(first_car_score, second_car_score)

print(f'The winner is {winner[0]} with total time: {winner[1]:.1f}')
