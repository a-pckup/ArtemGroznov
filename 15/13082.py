for a in range(0, 1000):
    flag = False
    for x in range(0, 400):
        for y in range(0, 400):
            f = (3 * x + y > 48) or (x > y) or (4 * x + y < a)
            if not f:
                flag = True
                break
        if flag:
            break
    if flag:
        print(a)
