for a in range(0, 1000):
    flag = True
    for x in range(90, 101):
        f = (not (x & 79 == 0)) and ((x & 31 == 0) <= (not (x & a == 0)))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)
