def f(n):
    s = ""
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s


p = 0
for n in range(343, 2402):
    b = f(n)
    if int(b[-1]) % 2 == 0:
        b = "6" + b
    else:
        b = "5" + b
    r = int(b, 7)
    if r > 14500:
        p += 1

print(p)