print("x y z w f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
               f = w and ((z or y) == (z and x))
               print(x, y, z, w, int(f))
