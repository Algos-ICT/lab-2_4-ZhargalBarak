def z_func(s):
    z = [''] * (len(s)-1)
    L = 0
    R = 0
    for i in range(1, len(s)):
        if i >= R:
            j = 0
            while i+j < len(s) and s[i+j] == s[j]:
                j += 1
            L = i
            R = i+j
            z[i-1] = str(j)
        else:
            if int(z[i-L-1]) < R-i:
                z[i-1] = z[i-L-1]
            else:
                j = R-i
                while i+j < len(s) and s[i+j] == s[j]:
                    j += 1
                L = i
                R = i+j
                z[i-1] = str(j)
    return z

with open('input.txt') as f:
    s = f.readline().strip()

Z = z_func(s)
with open('output.txt', 'w') as f:
    f.write(' '.join(Z))

