line = input()
k = int(input())

line_list = line.split()
counted_out = []

a = len(line_list)

counted_out_counter = 0
counter_iterations = 0

while counted_out_counter < a:
    for idx, i in enumerate(line_list):
        if line_list[idx] == '0':
            continue
        else:
            counter_iterations += 1

        if counter_iterations == k:
            counted_out_counter += 1
            counted_out.append(i)
            line_list[idx] = '0'
            counter_iterations = 0

new_list = [int(i) for i in counted_out]

print(str(new_list).replace(" ", ""))
