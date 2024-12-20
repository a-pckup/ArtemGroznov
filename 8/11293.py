from itertools import product

a = product("0123456789abc", repeat=6)
c = 0

for i in a:
    num = "".join(i)
    if num[0] != "0":
        if num.count("5") <= 1:
            for j in "13579b":
                num = num.replace(j, "*")
            if "**" not in num:
                c += 1

print(c)