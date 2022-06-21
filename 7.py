import random

def PolyHash(P, l, p, x):
    res = 0
    for i in reversed(range(l)):
        res = (res * x + ord(P[i])) % p
    return res % p


def PrecomputeHashes(T, l, k, p, x):
    H = [0] * (l - k + 1)
    S = T[l - k : l]
    H[l - k] = PolyHash(S, k, p, x)
    y = 1
    for i in range(1, k + 1):
        y = (y * x) % p
    for i in range(l -k - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + k]) + p) % p
    return H

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            exit()
        s, t = map(str, line.split())
        lS, lT = len(s), len(t)
        k = min(lS, lT)
        p = 10**9+7
        x = random.randint(1, p-1)
        flag = False
        for i in reversed(range(1, k+1)):
            Hs = PrecomputeHashes(s, lS, i, p, x)
            Ht = PrecomputeHashes(t, lT, i, p, x)
            for j in range(len(Hs)):
                for h in range(len(Ht)):
                    if Hs[j] == Ht[h]:
                        print(j, h, i)
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break
        if not flag:
            print(0, 1, 0)