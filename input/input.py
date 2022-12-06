from equations.base.equation import Equation


class InputReceiver:
    def _collect_float(self, arg_name) -> float:
        while True:
            received = input(f"Введите {arg_name}:\n")
            try:
                return float(received)
            except ValueError:
                print("Неверное значение, попробуйте еще раз...")

    def _collect_int(self, arg_name) -> int:
        while True:
            received = input(f"Введите {arg_name}:\n")
            try:
                return int(received)
            except ValueError:
                print("Неверное значение, попробуйте еще раз...")

    def collect_arguments(self, equation: Equation) -> list[float]:
        args = []
        for i in range(equation.argument_count):
            args.append(self._collect_float(equation.argument_names[i]))
        return args

    def collect_menu_item(self, choices: list[int]) -> int:
        while True:
            collected = self._collect_int("пункт меню")
            if collected in choices:
                return collected

    def collect_calculation_input(self, input_name) -> int:
        return self._collect_int(input_name)
