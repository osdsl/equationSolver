from equations.arithmetic_progression import ArithmeticProgression
from equations.base.equation import Equation
from equations.cubic_equation import CubicEquation
from equations.geometric_progression import GeometricProgression
from equations.linear_equation import LinearEquation
from equations.quadratic_equation import QuadraticEquation
from input.input import InputReceiver


class Menu:
    _data: list[float] = []
    _equator: Equation = None
    _input: InputReceiver

    def __init__(self):
        self._input = InputReceiver()

    def _get_equation_name(self):
        if self._equator is None:
            return "Не выбрано"
        return self._equator.equation_name

    def _consolidate_arguments(self):
        return zip(self._equator.argument_names, self._data)

    def _equation_selector(self):
        choices = [1, 2, 3, 4, 5, 0]
        while True:
            print("Выберите тип уравнения:")
            print("1. Линейное уравнение")
            print("2. Квадратное уравнение")
            print("3. Кубическое уравнение")
            print("4. Арифметическая прогрессия")
            print("5. Геометрическая прогрессия")
            print("0. Назад")

            choice = self._input.collect_menu_item(choices)

            match choice:
                case 0:
                    return
                case 1:
                    self._equator = LinearEquation()
                    self._data = []
                case 2:
                    self._equator = QuadraticEquation()
                    self._data = []
                case 3:
                    self._equator = CubicEquation()
                    self._data = []
                case 4:
                    self._equator = ArithmeticProgression()
                    self._data = []
                case 5:
                    self._equator = GeometricProgression()
                    self._data = []
            return

    def _list_arguments(self):
        print("Аргументы:")
        for argument in self._consolidate_arguments():
            print(f"{argument[0]}: {argument[1]}")

    def _calculate_equation(self):
        if self._equator.validate(self._data):
            if self._equator.is_progression:
                answer = self._equator.calculate("calc", self._input.collect_calculation_input("член прогрессии для "
                                                                                               "вычисления"))
            else:
                answer = self._equator.calculate()
            print(f"Ответ: {', '.join(map(lambda el: str(el), answer))}")
        else:
            print("Выбранные аргументы не могут быть использованы для этого типа уравнения. Выберите другие.")

    def _progression_sum(self):
        if self._equator.validate(self._data) and self._equator.is_progression:
            print(self._equator.calculate("sum", self._input.collect_calculation_input("количество членов прогрессии "
                                                                                       "для расчета суммы")))
        else:
            print("Выбранные аргументы не могут быть использованы для этого типа уравнения. Выберите другие.")

    def _set_arguments(self):
        if self._equator is None:
            print("Сначала установите уравнение!")
            return
        self._data = self._input.collect_arguments(self._equator)

    def run(self):
        print("Добро пожаловать в программу для решения уравнений")
        print("Используйте цифры на клавиатуре для навигации. Enter для отправки.")
        while True:
            print(f"Выбранное уравнение: {self._get_equation_name()}")

            if len(self._data) != 0:
                self._list_arguments()
            else:
                print("Аргументы не введены.")

            possible_entries = [8, 9, 0]
            if self._equator is not None:
                possible_entries.extend([1, 7])
                if self._equator.is_progression:
                    print("1. Найти член прогрессии")
                    print("2. Найти сумму членов прогрессии")
                    possible_entries.append(2)
                else:
                    print("1. Найти корни")
                print("7. Сгенерировать аргументы")

            print('8. Установить аргументы')
            print("9. Установить уравнение")
            print("0. Выход")

            choice = self._input.collect_menu_item(possible_entries)

            match choice:
                case 0:
                    return
                case 1:
                    self._calculate_equation()
                case 2:
                    self._progression_sum()
                case 7:
                    self._data = self._equator.generate_arguments()
                case 8:
                    self._set_arguments()
                case 9:
                    self._equation_selector()
