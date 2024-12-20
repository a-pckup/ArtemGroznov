from string import ascii_uppercase

alph = "0123456789" + ascii_uppercase[:11]

for x in alph:
    for y in alph:
        num1 = int("943697" + x + "21", 21)
        num2 = int("2" + y + "9253", 21)
        res = num1 - num2
        if res % 20 == 0:
            print(res // 20, int(x, 21) - int(y, 21))
