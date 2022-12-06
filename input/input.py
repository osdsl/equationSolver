from equations.base.equation import Equation


class InputReceiver:
    def collect_arguments(self, equation: Equation) -> list[float]:
        pass

    def collect_menu_item(self, choices: list[int]) -> int:
        pass

    def collect_calculation_input(self) -> int:
        pass


