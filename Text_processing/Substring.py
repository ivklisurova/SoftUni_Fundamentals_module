def solve(word,word_2):
    while word in word_2:
        word_2 = word_2.replace(word, '')

    print(word_2)


solve(input(),input())