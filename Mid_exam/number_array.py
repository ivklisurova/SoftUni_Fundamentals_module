numbers = list(map(int, input().split(' ')))

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'End':
        break
    elif command == 'Switch':
        index = int(tokens[1])
        if 0 <= index < len(numbers):
            numbers[index] = numbers[index] * -1
    elif command == 'Change':
        index = int(tokens[1])
        value = int(tokens[2])
        if 0 <= index < len(numbers):
            numbers[index] = value
    elif command == 'Sum':
        to_sum = tokens[1]
        if to_sum == 'All':
            print(sum(numbers))
        elif to_sum == 'Positive':
            sum_positive = 0
            for i in numbers:
                if i >= 0:
                    sum_positive += i
            print(sum_positive)
        elif to_sum == 'Negative':
            sum_negative = 0
            for i in numbers:
                if i < 0:
                    sum_negative += i
            print(sum_negative)

[print(x, end=' ') for x in numbers if x >= 0]
