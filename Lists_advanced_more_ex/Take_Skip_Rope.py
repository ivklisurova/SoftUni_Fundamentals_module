input_string = input()

numbers_list = [x for x in input_string if x.isdigit()]
non_numbers_list = [x for x in input_string if not x.isdigit()]

take_list = []
skip_list = []

for x, k in enumerate(numbers_list):
    if x % 2 == 0:
        take_list.append(k)
    else:
        skip_list.append(k)

decoded_string = []

for i, j in zip(take_list, skip_list):
    result_string = non_numbers_list[:int(i)]
    [non_numbers_list.remove(x) for x in result_string]
    [decoded_string.append(x) for x in result_string]
    skip_str = non_numbers_list[:int(j)]
    [non_numbers_list.remove(k) for k in skip_str]

[print(x, end='') for x in decoded_string]
