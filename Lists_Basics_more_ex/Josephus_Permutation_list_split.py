line = input()
k = int(input())

line_list = line.split()
lenght_list = len(line_list)

first_half = (len(line_list) // 2) - 1

list_1 = []
list_2 = []
counted_out_list = []
counter_counted_out = 0
counter_iterations = 0

while counter_counted_out < lenght_list:
    for idx, i in enumerate(line_list):
        if idx <= first_half:
            list_1.append(i)
        else:
            list_2.append(i)

    if counter_counted_out == lenght_list - 2:
        counted_out_list.append(list_1[0])
        counted_out_list.append(list_1[1])
        break
    else:
        counted_out_list.append(list_1[2])
        list_1.remove(list_1[2])
        line_list = list_2 + list_1
        counter_counted_out += 1
        list_1.clear()
        list_2.clear()

final_row_list = list(map(int, counted_out_list))
print(str(final_row_list).replace(" ", ""))
