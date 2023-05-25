x = int(input())

for _ in range(x):
    n = list(map(int, input().split(" ")))
    n.sort()
    print(n[1])