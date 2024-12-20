f = open("17550.txt")

c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_tr = [x for x in a if a.count(x) == 3]
    a_tr_kv = [x**2 for x in a_tr]
    a_r = [x for x in a if a.count(x) == 1]

    if len(a_tr) == 3 and len(a_r) == 3:
        if sum(a_tr)**2 > sum(a_r)**2:
            c += 1

print(c)