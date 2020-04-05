substring_list = input().split(', ')
string_list = input().split(', ')

new_list = []

for i in substring_list:
    for j in string_list:
        if i in j:
            if i in new_list:
                continue
            else:
                new_list.append(i)


print(new_list)