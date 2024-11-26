def f(n):
    s = ""
    while n > 0:
        s = str(n % 6) + s
        n //= 6
    return s


...
for x in range(1, 2031):
    a = ...
    b = f(a)
    ...