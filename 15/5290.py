for a in range(1, 500):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            f = (not ((x + 5 < a) <= (y > a))) or (x * y >= 76)
            if f == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)
