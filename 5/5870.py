p = []
for n in range(64, 10000):
    b = bin(n)[2:]
    s = b.count("1")
    if s % 2 == 0:
        t = b[-4:]
        t = t.replace("1", "*")
        t = t.replace("0", "1")
        t = t.replace("*", "0")
        b = b[:-4] + t
    else:
        t = b[-5:-1]
        t = t.replace("1", "*")
        t = t.replace("0", "1")
        t = t.replace("*", "0")
        b = b[:-5] + t + b[-1]
    r = int(b, 2)
    p.append([r, n])

print(min(p))