import re

pattern = r'(w{3}[.])(?<=.)([A-z0-9]*[-]*[A-z0-9]*)(([.][a-z]+)+)'

while True:
    text = input()
    if not text:
        break
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    ll_m = []
    for i in matches:
        for j in i:
            ll_m.append(j)
        if len(ll_m) > 0:
            print(''.join(ll_m[0:3]))

# check the regex there is a simplier way to do it :)