import math

cases = int(input())

for _ in range(cases):
    n, k = list(map(int, input().split(" ")))
#    print(min(min(n//i,n if n//i>k else i)
#    for i in range(1,min(int(n**.5),k)+1)if n%i==0))
    if k > n:
        print(1)
    elif k == 1:
        print(n)
    else:
        ans = 1
        for i in range(1, 1 + min(int(n**0.5), k)):
            if n % i == 0:
                if n/i <= k:
                    ans = max(ans, n/i)
                ans = max(ans, i)
        print(int(n/ans))