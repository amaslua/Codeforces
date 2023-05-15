x = input().split(' ')
n = int(x[0])
l = int(x[1])

lamps = input().split(' ')
lamps = [int(x) for x in lamps]

lamps.sort()
cur = lamps[0]
m = lamps[0]*2

for i in range(1, n):
    m = max(m, lamps[i]-cur)
    cur = lamps[i]
m = max((l-lamps[-1])*2, m)


print(m/2)