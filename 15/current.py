c = "123"

first = c[0]
last = c[-1]

c = last + c[1:-1] + first

print(c)