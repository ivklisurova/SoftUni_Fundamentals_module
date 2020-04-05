words = input().split()
searched_palindrome = input()

found_palindromes = [x for x in words if x[::-1] == x]

# for x in words:
#     if x[::-1] == x:
#         found_palindromes.append(x)



count_palindromes = found_palindromes.count(searched_palindrome)

print(found_palindromes)
print(f'Found palindrome {count_palindromes} times')
