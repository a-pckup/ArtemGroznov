f = open("12726.txt")

c = 0

for i in f:
    a = [int(x) for x in i.split()]
    c += 1
    a_p = [x for x in a if a.count(x) == 3]
    a_r = [x for x in a if a.count(x) == 1]
    a_ch = [x for x in a if x % 2 == 0]
    a_nech = [x for x in a if x % 2 != 0]
    if len(a_p) == 3 and len(a_r) == 4:
        if len(a_ch) > len(a_nech):
            print(c)
