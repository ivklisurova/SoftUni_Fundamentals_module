string_one = input()
string_two = input()

previous_str = ''

a = len(string_two)

for index in range(len(string_one)):
    current_string = ''
    for i in range(0, index + 1):
        current_string += string_two[i]
    for j in range(index + 1, len(string_one)):
        current_string += string_one[j]
    if current_string != previous_str:
        print(current_string)
        previous_str = current_string
