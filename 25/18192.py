def f(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


for num in range(1000000, 2000000):
    list_of_divs = f(num)
    list_prime_divs = []
    for i in list_of_divs:
        if len(f(i)) == 2:
            list_prime_divs.append(i)
    if len(list_prime_divs) == 3:
        print(num, max(list_prime_divs))