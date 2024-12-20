def f(n):
    s = []
    while n != 0:
        s.append(n % 27)
        n = n // 27
    return s

c = 0
n = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024
a = f(n)
for i in a:
    if i > 9:
        c += 1
print(c)