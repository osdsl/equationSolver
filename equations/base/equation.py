from abc import ABC, abstractmethod


class Equation(ABC):
    @property
    @abstractmethod
    def is_progression(self) -> bool:
        pass

    @property
    @abstractmethod
    def equation_name(self) -> str:
        return "Не выбрано"

    @property
    @abstractmethod
    def argument_names(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def argument_count(self) -> int:
        pass

    @abstractmethod
    def validate(self, data: list[float]) -> bool:
        pass

    @abstractmethod
    def calculate(self, additional_arg_type=None, additional_input=None) -> list[float]:
        pass
