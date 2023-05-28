n, a, b, c  = list(map(int, input().split(" ")))

m = min(a, min(b, c))

if n % m == 0:
    print(int(n/m))
else:
    num = n//m
    output = []

    for i in range(0, num+1):
        num2 = (n-i*a)//b
        for j in range(0, num2+1):
            if (n - i*a - j*b) % c == 0:
                next = int((n - i*a - j*b) / c)
                output.append(i+j+next)

    print(max(output))