p = []
for n in range(1, 1000):
    b = bin(n)[2:]
    summa = sum(map(int, list(b)))
    if summa % 2 == 0:
        b = "10" + b[2:] + "0"
    else:
        b = "11" + b[2:] + "1"
    r = int(b, 2)
    if r > 171:
        p.append(n)

print(min(p))