from itertools import product

a = product("01234567", repeat=5)
c = 0

for i in a:
    num = "".join(i)
    if num[0] != "0":
        if num.count("6") == 1:
            for j in "1357":
                num = num.replace(j, "*")
            if "*6" not in num and "6*" not in num:
                c += 1

print(c)