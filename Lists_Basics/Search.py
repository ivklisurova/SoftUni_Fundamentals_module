n = int(input())
word = input()

my_list = []

for i in range(n):
    given_string = input()
    my_list.append(given_string)

print(my_list)

for k in range(len(my_list) - 1, -1, -1):
    element = my_list[k]
    if word not in element:
        my_list.remove(element)
        print(len(my_list))

print(my_list)




