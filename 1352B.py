x = int(input())

for _ in range(x):
    y = list(map(int, input().split(" ")))
    a = int(y[0])
    b = int(y[1])
    if b > a:
        print ("NO")
    elif b == a:
        print("YES")
        out = ""
        for _ in range(a):
            out += "1 "
        print(out[:-1])
    elif a % b == 0:
        print("YES")
        out = ""
        n = int(a/b)
        for _ in range(b):
            out += str(n) + " "
        print(out[:-1])
    else:
        n1 = a - (b-1)
        if n1 > 0 and n1 % 2 == 1:
            print("YES")
            out = ""
            for _ in range(b-1):
                out += "1 "
            out += str(n1)
            print(out)
            continue
        n2 = a - 2*(b-1)
        if n2 > 0 and n2 % 2 == 0:
            print("YES")
            out = ""
            for _ in range(b-1):
                out += "2 "
            out += str(n2)
            print(out)
            continue
        print("NO")