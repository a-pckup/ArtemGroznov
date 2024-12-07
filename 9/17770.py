f = open("17770.txt").readlines()
c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_5 = [x for x in a if str(x)[-1] == "5"]

    b = sorted(a)
    if (b[4] + b[3]) * 2 > sum(b[:3]) * 3:
        if len(a_5) >= 2:
            c += 1

print(c)
