for p in range(10, 100):
    for x in range(p):
        for y in range(p):
            num1 = 9 * p**0 + x * p**1 + 4 * p**2 + 2 * p**3
            num2 = 3 * p**0 + y * p**1 + x * p**2 + y * p**3
            num3 = 0 * p**0 + y * p**1 + 4 * p**2 + x * p**3
            if num1 + num2 == num3:
                res = y * p**0 + y * p**1 + x * p**2
                print(res)
