p = []
for n in range(1, 10000):
    b = bin(n)[2:]
    s = b.count("1")
    b = b + str(s % 2)
    s = b.count("1")
    b = b + str(s % 2)
    r = int(b, 2)
    if r > 123:
        p.append(r)
print(min(p))