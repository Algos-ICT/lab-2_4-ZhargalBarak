import random

def PolyHash(P, p, x):
    res = 0
    for i in reversed(range(n)):
        res = (res * x + ord(P[i])) % p
    return res


def PrecomputeHashes(T, p, x):
    global n, m
    H = [0] * (m - n + 1)
    S = T[m - n : m]
    H[m - n] = PolyHash(S, p, x)
    y = 1
    for i in range(1, n + 1):
        y = (y * x) % p
    for i in range(m - n - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + n]) + p) % p
    return H


def RabinKarp(pattern, text):
    global n, m
    p = 10 ** 9 + 9
    x = random.randint(1, p-1)
    count = 0
    res = []
    hPattern = PolyHash(pattern, p, x)
    H = PrecomputeHashes(text, p, x)
    for i in range(m - n + 1):
        if hPattern != H[i]:
            continue
        count += 1
        res.append(str(i + 1))
    with open("output.txt", "w") as f:
        f.write(str(count) + "\n" + " ".join(res))


with open("input.txt") as f:
    P = f.readline()[:-1]
    T = f.readline()

n, m = len(P), len(T)
RabinKarp(P, T)

