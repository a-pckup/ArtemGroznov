def f(n):
    s = ""
    while n > 0:
        s = str(n % 6) + s
        n //= 6
    return s


p = []
for n in range(1, 100000):
    b = f(n)

    if n % 3 == 0:
        b = b + b[:2]
    else:
        b = b + f((n % 3) * 10)

    r = int(b, 6)
    if r > 680:
        p.append(r)

print(min(p))
