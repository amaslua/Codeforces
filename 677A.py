x = input()
y = input()
a = x.split(" ")
n = int(a[0])
h = int(a[1])
b = y.split(" ")

count = 0
for i in range(n):
    cur = int(b[i])
    count += -(-cur//h)
print(count)