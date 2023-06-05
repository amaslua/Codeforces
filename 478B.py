import math

n, m = list(map(int, input().split(" ")))

if n == m:
    print(0, 0)
else:
    ma = int(math.comb(n-m+1, 2))

    l = int(n/m)
    remainder = int((n/m - int(n/m)) * m+0.5)



    mi = math.comb(l+1, 2) * remainder
    mi += math.comb(l, 2) * (m-remainder)
    print(mi, ma)