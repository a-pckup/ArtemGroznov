def f(n):
    d=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    return list(d)
for i in range(18782, 18823):
    s=f(i)
    g=[]
    for x in s:
        if x%2!=0:
            g.append(x)
    if len(g)==3:
        print(*sorted(g))
