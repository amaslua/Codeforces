x = input()

out = ''

for i in range(len(x)):
    if i == 0 and x[i] == '9':
        out += x[i]
        continue
    if x[i] >= '5':
        n = 9-int(x[i])
        out += str(n)
    else:
        out += x[i]

print(out)