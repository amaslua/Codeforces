x = input()
y = input()
n = len(x)

check = True
for i in range(n):
    if x[i] != y[-1-i]:
        check = False
        break

if check:
    print("YES")
else:
    print("NO")