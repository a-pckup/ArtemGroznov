for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (x & 57 == 0) or ((x & 23 == 0) <= (not (x & a == 0)))
        if not f:
            flag = False
            break
    if flag:
        print(a)
