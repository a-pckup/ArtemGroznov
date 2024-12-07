def Del(num1, num2):
    return num1 % num2 == 0

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (not (Del(x,a))) <= (Del(x,14)<=(not(Del(x,4))))
        if not f:
            flag = False
            break
    if flag:
        print(a)