x = input().split(' ')
x = (int(a) for a in x)

n, m, a, b = x
cost = min(n//m * b, n//m * m * a)
cost += (n - n//m * m) * a
cost = min(cost, -(-n//m) * b)

print(int(cost))