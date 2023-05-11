x = int(input())

count = 0
for i in range(x):
    y = input().split(" ")
    if int(y[1]) - int(y[0]) >= 2:
        count += 1
print(count)