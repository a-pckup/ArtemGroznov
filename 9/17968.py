f = open('17968.txt')
c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_1_1 = sorted(a)
    a_ch = [x for x in a if x % 2 == 0]
    a_nch = [x for x in a if x % 2 != 0]
    if a_1_1[3] < (a[0] + a[1] + a[2]):
        if sum(a_2_1) == sum(a_2_2):
            c += 1
print(c)
