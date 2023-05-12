x = input()
y = input()

a = list(x)
b = list(y)
n = len(x)
out = ""

for i in range(n):
    if a[i] == b[i]:
        out += '0'
    else:
        out += '1'

print(out)