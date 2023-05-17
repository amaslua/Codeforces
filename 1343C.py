x = int(input())

for _ in range(x):
    n = int(input())
    a = list(map(int, input().split(' ')))

    m = 0
    cur = [a[0]]
    for i in range(1, n):
        if cur[-1] * a[i] > 0:
            cur.append(a[i])
        else:
            if cur[-1] > 0:
                m += max(cur)
            else:
                m += max(cur)
            cur = [a[i]]

    if cur[-1] > 0:
        m += max(cur)
    else:
        m += max(cur)
    print(m)