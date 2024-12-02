a = open("13865.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    b_r = [x for x in b if b.count(x) == 1]
    if len(b_r) == 7:
        if (bs[-1] + bs[0]) * 2 <= sum(bs[1:-1]) * 3:
            c += 1

print(c)
