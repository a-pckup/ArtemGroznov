p = []

for n in range(1, 101):
    b = bin(n)[2:]
    b = b[::-1]
    b = b[b.index("1"):]
    r = int(b, 2)
    if r == 7:
        p.append(n)

print(max(p))