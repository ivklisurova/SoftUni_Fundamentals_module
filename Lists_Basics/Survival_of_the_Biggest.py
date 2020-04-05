string_numbers = input()
n = int(input())

list_numbers = string_numbers.split()
int_list = list(map(int, list_numbers))

for i in range(n):
    a = min(int_list)
    int_list.remove(a)
print(int_list)
