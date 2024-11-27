s = "3" * 111

while "33333" in s or "1111" in s:
    if "33333" in s:
        s = s.replace("33333", "111", 3)
    else:
        s = s.replace("111", "33", 3)

summa = sum(map(int, list(s)))
print(summa)