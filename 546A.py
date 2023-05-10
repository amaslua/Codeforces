x = input()
y = x.split(" ")

k = int(y[0])
n = int(y[1])
w = int(y[2])

h = 0.5*w*(w+1)*k
if n > h:
    print(0)
else:
    print(int(0.5*w*(w+1)*k-n))