x = int(input())


for _ in range(x):
    a = list(map(int, input().split(" ")))
    if a[0] + a[1] == a[2]:
        print("+")
    else:
        print("-")
