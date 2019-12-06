import re

alpha = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input()
res = ''
for c in s:
    k = re.findall(r'[abcdefghijklmnopqrstuvwxyz]', c)
    if k != []:
        res += alpha[(alpha.index(c) + n) % len(alpha)]
    else:
        res += c
print('Result: "' + res + '"')