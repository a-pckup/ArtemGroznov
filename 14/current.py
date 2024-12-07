from string import ascii_lowercase

alph = "0123456789" + ascii_lowercase

for p in range(10,37):
    for x in alph[:p]:
        for y in alph[:p]:
            a = int("24" + x + "9", p)