import math

n = int(input())
num = list(map(int, input().split(" ")))
if max(num) == min(num):
    out = "0 "
    out += str(int(n*(n-1)/2))
    print(out)

else:

    mi = 9999999999999
    ma = 0
    c_mi = 0
    c_ma = 0


    for i in num:
        if i < mi:
            mi = i
            c_mi = 1
        elif i == mi:
            c_mi += 1
        if i > ma:
            ma = i
            c_ma = 1
        elif i == ma:
            c_ma += 1

    diff = ma-mi
    if ma == mi:
        c = math.factorial(c_mi-1)
    else:
        c = c_mi * c_ma

    out = str(diff)
    out += " "
    out += str(c)
    print(out)