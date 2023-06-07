import math

cases = int(input())

for _ in range(cases):
    n, k = list(map(int, input().split(" ")))
    n_copy = n
    if k > n:
        print(1)
    elif k == 1:
        print(n)
    else:
        for i in range(min(int(math.sqrt(n)), k), 1, -1):
            if n % i == 0:
                print(min(int(n/i), i))
                break