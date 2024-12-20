def f(n):
    d=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    return list(d)

for i in range(900001, 1800000):
    s=f(i)
    if not s:
        continue
    m=max(s) + min(s)
    if str(m)[-2:] == "46":
        print(i,m)
