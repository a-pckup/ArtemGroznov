def f(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

p = []
for n in range(1, 1000):
    b = f(n)
    if n % 3 == 0:
        b = "1" + b + "02"
    else:
        b = b + f((n % 3) * 4)
    r = int(b, 3)
    if r < 199:
        p.append(n)

print(max(p))