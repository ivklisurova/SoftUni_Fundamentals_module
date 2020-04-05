text = input()

#[(f':{i[i.index(":")+1]}') for i in text if i == ':']

for i in text:
    if i == ':':
        print(f':{text[i.index(":")+1]}')