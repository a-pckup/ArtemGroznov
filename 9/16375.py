f = open("16375.txt")

c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_dv = [x for x in a if a.count(x) == 2]
    a_nep = sorted([x for x in a if a.count(x) == 1])
    if len(a_dv) == 2 and len(a_nep) == 5:
        if a_nep[0] * a_nep[1] * a_nep[2] > a_dv[1] ** 2:
            c += 1

print(c)
