def DEL(n, m):
    return n % m == 0


for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (not DEL(x, a)) <= (DEL(x, 28) <= (not DEL(x, 49)))
        if not f:
            flag = False
            break
    if flag:
        print(a)
