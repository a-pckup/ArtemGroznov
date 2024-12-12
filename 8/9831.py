from itertools import product

a = product("0123456789abcdef", repeat=3)

c = 0

for i in a:
    num = "".join(i)
    if num[0] != "0":
        if len(num) == len(set(num)):
            for j in "02468ace":
                num = num.replace(j, "*")
            for j in "13579bdf":
                num = num.replace(j, "-")
            if "**" not in num and "--" not in num:
                c += 1

print(c)
