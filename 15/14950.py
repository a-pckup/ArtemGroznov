from math import gcd


def nod(n, m, k):
    if gcd(n, m) == k:
        return True
    else:
        return False


c = 0
for a in range(1, 1001):
    flag = True
    for x in range(1, 1000):
        f = nod(a, 420, 2) or ((not nod(a, x, 12)) <= (not nod(110, x, 11))) and (not (a in range(5, 138)))
        if f == 0:
            flag = False
            break
    if flag == True:
        c += 1

print(c)