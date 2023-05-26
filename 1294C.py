import math

x = int(input())

for _ in range(x):
    n = int(input())
    f = []
    used = []
    for _ in range(2):
        x = 2
        while x < n:
            if n % x == 0 and x not in used:
                f.append(x)
                used.append(x)
                n = n/x
                break
            elif x > math.sqrt(n):
                break
            else:
                x += 1
    f.append(int(n))
    if len(f) == 3 and len(set(f)) == 3:
        print('YES')
        out = ""
        for i in f:
            out += str(i)
            out += " "
        print(out[:-1])
    else:
        print('NO')