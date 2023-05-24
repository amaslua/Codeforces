x1, y1, x2, y2 = list(map(int, input().split(" ")))

if x1 == x2:
    height = abs(y1 - y2)
    if height == 0:
        print(-1)
    else:
        x3 = x1 + height
        print(x3, y1, x3, y2)

elif y1 == y2:
    width = abs(x1 - x2)
    if width == 0:
        print(-1)
    else:
        y3 = y1 + width
        print(x1, y3, x2, y3)

else:
    if abs(x1-x2) != abs(y1-y2):
        print(-1)
    else:
        print(x1, y2, x2, y1)