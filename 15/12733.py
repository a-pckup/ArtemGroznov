for a in range(1, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x > 56) or (y >= x) or (3 * x - y < a)
            if f == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)
