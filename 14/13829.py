for x in "0123456789abcdefgh":
    num1 = int("71" + x + "264", 18)
    num2 = int("4" + x + "51" + x + "1", 18)
    num3 = int("21" + x + "637", 18)
    result = num1 + num2 + num3
    if result % 17 == 0:
        print(result // 17)