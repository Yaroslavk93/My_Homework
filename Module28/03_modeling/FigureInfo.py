from abc import ABC, abstractmethod
from typing import Any


class Figure(ABC):
    """Абстрактный класс, определяющий значения 2D фигур"""
    def __init__(self, name: str, h: Any, base: Any) -> None:
        self._name = name
        self.h = h
        self.base = base
        self.base_area = self.base ** 2

    @abstractmethod
    def find_perimeter(self) -> float:
        pass

    @abstractmethod
    def find_area(self) -> float:
        pass

    @property
    def perimeter(self) -> str:
        return f'{self._name}: Периметр = {round(self.find_perimeter(), 2)}'

    @property
    def area(self) -> str:
        return f'{self._name}: Площадь = {self.find_area()}'


