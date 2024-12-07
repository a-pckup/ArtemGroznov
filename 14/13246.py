for p in range(10, 100):
    for x in range(p):
        for y in range(p):
            num1 = 9 * p**0 + x * p**1 + 4 * p**2 + 2 * p**3
            num2 = 3 * p**0 + y * p**1 + x * p**2 + y * p**3
            num3 = 0 * p**0 + y * p**1 + 4 * p**2 + x * p**3
            if num1 + num2 == num3:
                res = y * p**0 + y * p**1 + x * p**2
                print(res)

from string import ascii_lowercase

alph = "0123456789" + ascii_lowercase

for p in range(10, 37):
    for x in alph[:p]:
        for y in alph[:p]:
            num1 = int("24" + x + "9", p)
            num2 = int(y + x + y + "3", p)
            num3 = int(x + "4" + y + "0", p)
            if num1 + num2 == num3:
                res = int(x + y + y, p)
                print(res)






