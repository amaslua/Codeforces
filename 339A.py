x = input()
num = []
for i in range(0, len(x), 2):
    cur = x[i]
    num.append(cur)
num.sort()
out = str(num[0])
for n in num[1:]:
    out += "+"
    out += str(n)

print(out)