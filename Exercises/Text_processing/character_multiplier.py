string = input().split()
string_one = string[0]
string_two = string[1]

total_result = 0

min_word = min(len(string_one), len(string_two))

for i in range(min_word):
    total_result += ord(string_one[i]) * ord(string_two[i])

max_word = string_two

if len(string_one)>len(string_two):
    max_word = string_one

for x in range(min_word,len(max_word)):
    total_result += ord(max_word[x])

print(total_result)
