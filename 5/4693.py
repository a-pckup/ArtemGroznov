p = []
for n in range(1, 1000):
    b = bin(n)[2:]
    s = sum(map(int, list(b)))
    if s % 2 == 0:
        b = "10" + b[2:] + "0"
    else:
        b = "11" + b[2:] + "1"
    r = int(b, 2)
    if r > 40:
        p.append(n)
print(min(p))
