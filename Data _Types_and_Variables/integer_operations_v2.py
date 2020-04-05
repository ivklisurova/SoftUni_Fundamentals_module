first_num = int(input())
second_num = int(input())
third_num = int(input())
fourth_num = int(input())

def solve (num_1,num_2, num_3, num_4):
    result = ((num_1+num_2)//num_3)*num_4
    return result

print(solve(first_num,second_num,third_num,fourth_num))
