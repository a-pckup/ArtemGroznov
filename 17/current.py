f = open("17.txt")

a = [int(x) for x in f]
mn = min([x for x in a if str(x)[-1] == "6"])
b = []

for i in range(len(a) - 1):
    k = [a[i], a[i + 1], a[i + 2], a[i + 3]]
    l = [x for x in k if str(x)[-1] == "6"]
    if len(l) >= 2:
        if k[0]**2 + k[1]**2 < mn**2:
            b.append(k[0]**2 + k[1]**2)

print(len(b), max(b))












