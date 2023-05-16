a = int(input())
x = list(map(int, input().split(' ')))

b = int(input())
y = list(map(int, input().split(' ')))

for i in range(1, a):
    x[i] = x[i] + x[i-1]

def f(j):
    left = 0
    right = a-1

    while left < right:
        mid = (left + right) // 2
        if j == x[mid]:
            return mid+1
        if left+1 == right:
            if j <= x[left]:
                return left+1
            elif x[left] < j <= x[right]:
                return right+1
        if j < x[mid]:
            right = mid
        elif j > x[mid]:
            left = mid

for j in y:
    print(f(j))