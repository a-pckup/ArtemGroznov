def f(n, ss=5):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s


for x in range(1, 10000):
    var = 3**2000 + 3**10 - x
    tr = f(var)
    if tr.count(2) == 2000:
        print(x)
