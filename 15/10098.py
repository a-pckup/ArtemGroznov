for a in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x + 2 * y < a) or (y > x) or (x > 60)
            if f == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)