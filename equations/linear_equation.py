from equations.base.equation import Equation


class LinearEquation(Equation):
    _data = {}

    @property
    def is_progression(self) -> bool:
        return False

    @property
    def equation_name(self) -> str:
        return "Линейное уравнение"

    @property
    def argument_names(self) -> list[str]:
        return ["a", "b"]

    @property
    def argument_count(self) -> int:
        return 2

    def validate(self, data: list[float]) -> bool:
        if len(data) != self.argument_count:
            return False
        self._data = {"a": data[0], "b": data[1]}
        return True

    def calculate(self, additional_arg_type=None, additional_input=None) -> list[float]:
        return [-self._data["b"] / self._data["a"]]
