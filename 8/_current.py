from itertools import product

a = product("0123456789abcd", repeat=5)
c = 0

for i in a:
    num = "".join(i)
    if num[0] != "0":
        if num.count("9") == 1:
            if (num.count("b") + num.count("c") + num.count("d")) <= 3:
                c += 1

print(c)