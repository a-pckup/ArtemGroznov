for a in range(0, 1000):
    flag = True
    for x in range(0, 400):
        for y in range(0, 400):
            f = (x <= 19) or (y < 2 * x + a - 50) or (y > 17)
            if not f:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)