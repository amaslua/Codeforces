n = int(input())

stones = list(map(int, input().split(" ")))
stones_sort = stones.copy()
stones_sort.sort()

for i in range(1,n):
    stones[i] += stones[i-1]
    stones_sort[i] += stones_sort[i-1]

stones.insert(0, 0)
stones_sort.insert(0, 0)

m = int(input())

for _ in range(m):
    type, l, r = list(map(int, input().split(" ")))
    if type == 1:
        cur = stones[r] - stones[l-1]
        print(cur)
    else:
        cur = stones_sort[r] - stones_sort[l-1]
        print(cur)