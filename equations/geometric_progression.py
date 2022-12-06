import math

from equations.base.equation import Equation


class GeometricProgression(Equation):
    _data = {}

    @property
    def is_progression(self) -> bool:
        return True

    @property
    def equation_name(self) -> str:
        return "Геометрическая прогрессия"

    @property
    def argument_names(self) -> list[str]:
        return ["Первый член", "Шаг"]

    @property
    def argument_count(self) -> int:
        return 2

    def validate(self, data: list[float]) -> bool:
        if len(data) != self.argument_count:
            return False
        self._data = {'first': data[0], 'step': data[1]}
        return True

    def calculate(self, additional_arg_type=None, additional_input=None) -> list[float]:
        if additional_arg_type == "calc":
            return [self._data["first"] * math.pow(self._data["step"], additional_input - 1)]
        else:
            return [(self._data["first"] * (math.pow(self._data["step"], additional_input) - 1)) / (self._data["step"] - 1)]
