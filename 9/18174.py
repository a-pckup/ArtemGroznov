a = [14213, 2123, 34213, 4125, 5645, 675675, 73463, 87457, 93465]

b = [x for x in a if sum(map(int, list(str(x)))) % 2 == 0]

print(b)