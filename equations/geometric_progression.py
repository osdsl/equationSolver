from equations.base.equation import Equation


class GeometricProgression(Equation):
    @property
    def is_progression(self) -> bool:
        return True

    @property
    def equation_name(self) -> str:
        return "Геометрическая прогрессия"

    @property
    def argument_names(self) -> list[str]:
        return ["первый член", "шаг"]

    @property
    def argument_count(self) -> int:
        return 2

    def validate(self, data: list[float]) -> bool:
        pass

    def calculate(self, additional_arg_type=None, additional_input=None) -> list[float]:
        pass