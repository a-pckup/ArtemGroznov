for a in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x**2 + y**2 > 1024 - x) or (y < -2 * x + a)
            if f == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)
