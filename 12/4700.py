def f(n):
    p = []
    for i in range(2, n):
        if n % i == 0:
            p.append(i)
    if len(p) == 0:
        return True
    else:
        return False


for n in range(1, 1000):
    s = ">" + 39 * "0" + n * "1" + 39 * "2"
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    s = s.replace(">", "")
    summa = sum(map(int, list(s)))
    if f(summa) == True:
        print(n)
