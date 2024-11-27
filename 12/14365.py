p = [0]

for n in range(4, 10000):
    s = "7" + n * "3"

    while "73" in s or "3333" in s or "1133" in s:
        if "73" in s:
            s = s.replace("73", "11", 1)
        if "3333" in s:
            s = s.replace("3333", "7", 1)
        if "1133" in s:
            s = s.replace("1133", "37", 1)

    summa = sum(map(int, list(s)))

    if summa == 128:
        p.append(n)

    print(max(p))