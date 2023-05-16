import collections
x = int(input())

for _ in range(x):
    n = int(input())
    a = list(map(int, input().split(' ')))
    out = 0
    x = collections.defaultdict(int)
    for i in range(n):
        cur = a[i] - i
        out += x[cur]
        x[cur] += 1
    print(out)