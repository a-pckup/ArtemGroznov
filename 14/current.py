x_1 = "111"
x_2 = "21"

def f(n, ss):
    s = ""
    while n > 0:
        s = str(n % ss) + s
        n //= ss
    return s

print(f(1001, 3))