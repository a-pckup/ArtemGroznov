for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        f = (x & 30 != 4) or ((x & 35 == 1) <= (x & a == 0))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)