f = open('14250.txt')
s = []
c = 0
for i in f:
    a = [int(x) for x in i.split()]
    c += 1
    a_dif = sorted([x for x in a if a.count(x) == 1])
    if len(a_dif) == 6:
        if (a[-1] - a[0])**3 >= (a[1] + a[2] + a[3] + a[4])**2:
            s.append(c)
print(sum(s))