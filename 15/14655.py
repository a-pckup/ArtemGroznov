for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (x & a != 0) <= ((x & 168 == 0) <= (x & 69 != 0))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)