a = open("17863.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    b_tri = [x for x in b if b.count(x) == 3]
    b_razl = [x for x in b if b.count(x) == 1]
    if len(b_tri) == 3 and len(b_razl) == 3:
        if sum(b_tri) ** 2 > sum(b_razl) ** 2:
            c += 1
print(c)
