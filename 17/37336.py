f = open("17 (7).txt")

a = [int(x) for x in f]
p = []

for i in range(len(a) - 1):
    k = [a[i], a[i + 1]]
    if k[0] % 3 == 0 or k[1] % 3 == 0:
        p.append(sum(k))

print(len(p), max(p))