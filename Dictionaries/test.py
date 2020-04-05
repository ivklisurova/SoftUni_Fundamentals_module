a = input()

try:
    a = float(a)
    print('Yes')
except ValueError:
    print ("Not a float")