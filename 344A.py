x = int(input())

count = 1
cur = input()

for i in range(x-1):
    next = input()
    if cur[1] == next[0]:
        count += 1
    cur = next
print(count)