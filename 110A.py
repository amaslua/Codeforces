x = input()
c = 0

for i in x:
    if i == '4' or i == '7':
        c += 1
    if c > 7:
        break

if c == 4 or c == 7:
    print('YES')
else:
    print('NO')