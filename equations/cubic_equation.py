from equations.base.equation import Equation
import math


class CubicEquation(Equation):
    _data = {}

    @property
    def is_progression(self) -> bool:
        return False

    @property
    def equation_name(self) -> str:
        return "Кубическое уравнение"

    @property
    def argument_names(self) -> list[str]:
        return ["a", "b", "c", "d"]

    @property
    def argument_count(self) -> int:
        return 4

    def validate(self, data: list[float]) -> bool:
        if len(data) != self.argument_count:
            return False
        self._data = {'a': data[0], 'b': data[1], 'c': data[2], 'd': data[3]}
        return True

    def calculate(self, additional_arg_type=None, additional_input=None) -> list[float]:
        return self._solve(self._data["a"], self._data["b"], self._data["c"], self._data["d"])

    def _solve(self, a, b, c, d):

        if a == 0 and b == 0:
            return [(-d * 1.0) / c]

        elif a == 0:
            D = c * c - 4.0 * b * d
            if D >= 0:
                D = math.sqrt(D)
                x1 = (-c + D) / (2.0 * b)
                x2 = (-c - D) / (2.0 * b)
                return [x1, x2]
            else:
                return []

        f = self._findF(a, b, c)
        g = self._findG(a, b, c, d)
        h = self._findH(g, f)

        if f == 0 and g == 0 and h == 0:
            if (d / a) >= 0:
                x = (d / (1.0 * a)) ** (1 / 3.0) * -1
            else:
                x = (-d / (1.0 * a)) ** (1 / 3.0)
            return [x, x, x]

        elif h <= 0:
            i = math.sqrt(((g ** 2.0) / 4.0) - h)
            j = i ** (1 / 3.0)
            k = math.acos(-(g / (2 * i)))
            L = j * -1
            M = math.cos(k / 3.0)
            N = math.sqrt(3) * math.sin(k / 3.0)
            P = (b / (3.0 * a)) * -1

            x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
            x2 = L * (M + N) + P
            x3 = L * (M - N) + P

            return [x1, x2, x3]

        elif h > 0:
            R = -(g / 2.0) + math.sqrt(h)
            if R >= 0:
                S = R ** (1 / 3.0)
            else:
                S = (-R) ** (1 / 3.0) * -1
            T = -(g / 2.0) - math.sqrt(h)
            if T >= 0:
                U = (T ** (1 / 3.0))
            else:
                U = ((-T) ** (1 / 3.0)) * -1

            x1 = (S + U) - (b / (3.0 * a))
            return [x1]

    def _findF(self, a, b, c):
        return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0

    def _findG(self, a, b, c, d):
        return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a ** 2.0)) + (27.0 * d / a)) / 27.0

    def _findH(self, g, f):
        return (g ** 2.0) / 4.0 + (f ** 3.0) / 27.0
