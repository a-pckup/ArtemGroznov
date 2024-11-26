from itertools import product


s = 0
sim = '0123456789ABCD'
ar = product(sim, repeat=5)

for i in ar:
    num = "".join(i)
    if num[0] != "0":
        if num.count("9") == 1:
            if (num.count("B") + num.count("C") + num.count("D")) <= 3:
                s += 1

print(s)