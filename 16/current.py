for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (x & 57 == 0) or ((x & 23 == 0) <= (not (x & a == 0)))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)