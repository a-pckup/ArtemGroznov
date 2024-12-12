for a in range(-500, 500):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            f = (x * y < 2 * a) or (x >= 11) or (x < 2 * y)
            if f == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)
