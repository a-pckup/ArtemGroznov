import time

def timer(func):
    def wrapper(n):
        st = time.time()
        func(n)
        et = time.time()
        print(et -st)
    return wrapper


@timer
def f_1(n):
    z = []
    for i in range(1, n + 1):
        if n % i == 0:
            z.append(i)
    print(z)


@timer
def f_2(n):
    z = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            z.append(i)
    print(z)


@timer
def f_3(n):
    z = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            z.add(i)
            z.add(n // i)
    print(list(z))






# f_1(10_000_000)
# f_2(10_000_000)
f_3(100000_000_000_000)

10_000_000