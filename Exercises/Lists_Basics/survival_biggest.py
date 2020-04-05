numbers = input().split()
n = int(input())

int_list = [int(i) for i in numbers]

[int_list.remove(min(int_list)) for i in range(n)]

print(int_list)
