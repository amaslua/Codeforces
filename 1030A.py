x = int(input())
y = input()
z = y.split(" ")


check = True
for i in range(x):
    cur = z[i]
    if cur == '1':
        check = False
        break

if check:
    print("EASY")
else:
    print("HARD")