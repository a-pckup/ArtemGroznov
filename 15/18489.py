def cif(x, y):
    if str(x)[-1] == str(y)[-1]:
        return True
    else:
        return False

с = 0
for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = ((not cif(x, 5)) and cif(x, 4)) <= (x > a - 11)
        if f == False:
            flag = False
            break
    if flag == True:
        print(a)