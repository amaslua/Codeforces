x = input()

u = 0
l = 0

for i in x:
    if i == i.upper():
        u += 1
    else:
        l += 1

if l >= u:
    print(x.lower())
else:
    print(x.upper())