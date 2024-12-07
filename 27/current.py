def lineU(k, b):
    if k == 0:
        if b == 0:
            return "Бесконечно много решений"
        else:
            return "Нет корней"
    else:
        x = -b / k
        return f"Корень уравнения x = {x}"
    pass


def kwadr(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент a не должен быть равен 0.")
    else:
        d = b ** 2 - 4 * a * c
        koren1 = float('{:.3f}'.format((-b + (d ** 0.5)) / (2 * a)))
        koren2 = float('{:.3f}'.format((-b - (d ** 0.5)) / (2 * a)))
        return [koren1, koren2]


class function:
    def init(self, k, b):
        self.k = k
        self.b = b

    @classmethod
    def line(cls):
        print("Введите коэффиценты линейного уравнения kx + b = 0.")
        k = int(input("Введите k:"))
        b = int(input("Введите b:"))
        result = lineU(k, b)
        return result
        pass

    @classmethod
    def kwadrat(cls):
        print("Введите коэффиценты квадратного уравнения ах**2 + bх + с = 0. ")
        a = int(input("Введите а:"))
        b = int(input("Введите b:"))
        c = int(input("Введите c:"))
        result = kwadr(a, b, c)
        return result
        pass


a = function
print(a.line())