l = int(input())
stones = input()
count = 0

for i in range(l-1):
    cur = stones[i]
    next = stones[i+1]
    if cur == next:
        count += 1

print(count)