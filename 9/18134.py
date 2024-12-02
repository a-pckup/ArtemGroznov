from math import prod

f = open("18134.txt")

c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_p = [x for x in a if a.count(x) == 2]
    a_np = [x for x in a if a.count(x) == 1]
    if len(a_p) == 4 and len(a_np) == 2:
        if max(a_p) ** 2 > prod(a_np):
            c += 1

print(c)
