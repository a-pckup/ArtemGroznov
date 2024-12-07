def DEL(num1, num2):
    return num1 % num2 == 0

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = DEL(x, a) or ((70 <= x <= 90) <= (not (DEL(x, 22))))
        if not f:
            flag = False
            break
    if flag:
        print(a)
s