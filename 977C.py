n, k = list(map(int, input().split(" ")))

num = list(map(int, input().split(" ")))

num.sort()

if k == 0:
    if num[0] == 1:
        print(-1)
    else:
        print(num[0] - 1)
elif n == k:
    print(num[-1])
elif num[k-1] == num[k]:
    print(-1)  
else:
    print(num[k-1])