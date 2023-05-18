x = int(input())

for _ in range(x):
    z = list(map(int, input().split(' ')))
    n = z[0]
    x = z[1]

    odd = 0
    even = 0
    num = list(map(int, input().split(" ")))
    for cur in num:
        if cur % 2 == 0:
            even += 1
        else:
            odd += 1

    if n == x:
        if odd % 2 == 0:
            print("No")
        else:
            print("Yes")
    
    else:
        check = False
        for i in range(1, odd+1, 2):
            if x - i <= even and x - i >= 0:
                check = True
                break
        if check:
            print("Yes")
        else:
            print("No")