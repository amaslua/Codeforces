x = int(input())
n = list(map(int, input().split(" ")))

left = None
right = None

for i in range(x-1):
    if n[i] > n[i+1]:
        if left == None:
            left = i
        right = i+1

if left == None:
    print('yes')
    print('1 1')
else:
    rev = n[left:right+1]
    rev.reverse()
    n[left:right+1] = rev
    check = True
    for i in range(x-1):
        if n[i] > n[i+1]:
            check = False
            break
    if check:
        print('yes')
        out = ""
        out += str(left+1)
        out += " "
        out += str(right+1)
        print(out)
    else:
        print('no')