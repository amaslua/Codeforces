x = input()
queue = input()
y = x.split(" ")
n = int(y[0])
time = int(y[1])
queue = list(queue)

for t in range(time):
    i = 0
    while i < n-1:
        if queue[i] == 'B' and queue[i+1] == 'G':
            queue[i] = 'G'
            queue[i+1] = 'B'
            i += 1
        i += 1

out = "".join(queue)
print(out)