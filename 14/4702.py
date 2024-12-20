for x in "0123456789abcde":
    num1 = int("123" + x + "5", 15)
    num2 = int("1" + x + "233", 15)
    res = num1 + num2
    if res % 14 == 0:
        print(res // 14)