x = input()
y = x.split(" ")
a = int(y[0])
b = int(y[1])

count = 0

while a <= b:
    a = 3*a
    b = 2*b
    count += 1

print(count)