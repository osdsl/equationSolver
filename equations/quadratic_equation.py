import math

from equations.base.equation import Equation


class QuadraticEquation(Equation):
    _data = {}

    @property
    def is_progression(self) -> bool:
        return False

    @property
    def equation_name(self) -> str:
        return "Квадратное уравнение"

    @property
    def argument_names(self) -> list[str]:
        return ["a", "b", "c"]

    @property
    def argument_count(self) -> int:
        return 3

    def validate(self, data: list[float]) -> bool:
        if len(data) != self.argument_count:
            return False
        self._data = {"a": data[0], "b": data[1], "c": data[2]}
        return True

    def calculate(self, additional_arg_type=None, additional_input=None) -> list[float]:
        D = math.pow(self._data["b"], 2) - (4 * self._data["a"] * self._data["c"])
        if D < 0:
            return []
        elif D == 0:
            return [-(self._data["b"] / (2 * self._data["a"]))]
        else:
            x1 = (-self._data["b"] + math.sqrt(D)) / (2 * self._data["a"])
            x2 = (-self._data["b"] - math.sqrt(D)) / (2 * self._data["a"])
            return [x1, x2]
