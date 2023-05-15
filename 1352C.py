n = int(input())

for _ in range(n):
    n, k = list(map(int, input().split(' ')))
    print((k-1)//(n-1) + k)