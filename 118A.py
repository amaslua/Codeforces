x = input()
x = x.lower()


out = ''

for i in x:
    if i in ['a', 'e', 'i', 'o', 'u', 'y']:
        pass
    else:
        out += '.'
        out += i

print(out)