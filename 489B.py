x = int(input())

boys = input().split(' ')
boys = [int(x) for x in boys]
boys.sort()

y = int(input())
girls = input().split(' ')
girls = [int(x) for x in girls]
girls.sort()


count = 0
for i in range(x):
    for j in range(y):
        if -1 <= boys[i] - girls[j] <= 1:
            count += 1
            girls[j] = 1000
            break

print(count)