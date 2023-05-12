x = int(input())
y = input()
l = y.split(" ")

out = []
for i in range(1, x+1):
    out.append(str(1 + l.index(str(i))))

print(" ".join(out))