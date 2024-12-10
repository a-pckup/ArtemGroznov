for k1 in range(1, 55):
    for k2 in range(1, 55):
        for k3 in range(1, 28):
            s = "0" + k1 * "1" + k2 * "2" + k3 * "3" + "0"
            while "00" not in s:
                s = s.replace("01", "210", 1)
                s = s.replace("02", "320", 1)
                s = s.replace("03", "3012", 1)
            if s.count("1") == 26 and s.count("2") == 54 and s.count("3") == 48:
                print(2 + k1 + k2 + k3)
