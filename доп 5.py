with open('../1/input.txt') as f:
    t = f.readline()[:-1]
    p = f.readline()[:-1]

res = []
for i in range(len(t) - len(p) + 1):
    if t[i] == p[0]:
        part = t[i:i+len(p)]
        if part == p:
            res.append(str(i))

print(' '.join(res))

