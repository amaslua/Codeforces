x = input()
y = x.split(" ")

num = int(y[0])
t = int(y[1])

for x in range(t):
    if str(num)[-1] == '0':
        num = int(num/10)
    else:
        num -= 1
print(num)