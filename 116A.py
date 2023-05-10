x = int(input())
l = []
cur = 0

for i in range(x):
    y = input()
    z = y.split(" ")
    exit = int(z[0])
    enter = int(z[1])
    cur = cur + enter - exit
    l.append(cur)

print(max(l))