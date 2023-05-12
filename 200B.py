x = int(input())
y = input()
z = y.split(' ')


sum = 0
for i in range(x):
    sum += int(z[i])
print(sum/x)
