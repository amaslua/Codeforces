n = int(input())
x = list(map(int, input().split(' ')))


m = sum(x)
changed = False
for i in range(n):
    for j in range(i, n):
        before = x[0:i]
        after = x[j:]
        between = x[i:j+1]
        b = len(between) - sum(between)
        new = sum(before) + sum(after) + b
        if m != new:
            same = False
        else:
            same = True
        m = max(m, new)
        if m == new and not same:
            changed = True
if not changed:
    m -= 1

print(m)