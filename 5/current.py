p = []
for n in range(4, 10000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin(n % 3 * 3)[2:]
    r = int(b, 2)
    if r <= 138:
        p.append(r)

print(max(p))
