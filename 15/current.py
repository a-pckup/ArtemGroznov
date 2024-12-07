for a in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        f = (x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))
        if f == False:
            flag = False
            break
    if flag == True:
        print(a)