for a in range(1000, -1, -1):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = not ((x < 7) or (y >= 3 * x + a - 20) or (x >= 34) or (y < 121))
            if f == 1:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)