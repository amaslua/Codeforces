import math

n, m = list(map(int, input().split(" ")))

if n == m:
    print(0, 0)
else:
    ma = int(math.comb(n-m+1, 2))

    l = [int(n/m)] * m
    remainder = int((n/m - int(n/m)) * m+0.5)



    mi = 0
    for i in l:
        if remainder > 0:
            mi += math.comb(i+1, 2)
            remainder -= 1
        else:
            mi += math.comb(i, 2)

    print(mi, ma)