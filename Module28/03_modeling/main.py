from typing import Any, Iterator
from FigureInfo import Figure
from math import sqrt


class Triangle(Figure):
    """Класс, определяющий Периметр и Площадь треугольника"""
    def find_perimeter(self) -> float:
        side = sqrt((self.base / 2)**2 + self.h**2)
        _perimeter = self.h + side * 2
        return _perimeter

    def find_area(self) -> float:
        _area = 0.5 * self.h * self.base
        return _area


class Square(Figure):
    """Класс, определяющий Периметр и Площадь треугольника"""
    def __init__(self, name: str, side: Any) -> None:
        super().__init__(name, side, side)

    def find_perimeter(self) -> float:
        _perimeter = 4 * self.base
        return _perimeter

    def find_area(self) -> float:
        _area = self.base**2
        return _area


class VolumetricMixin:
    """Класс-примесь, определяющий площадь 3D фигур"""
    amount = 0
    @classmethod
    def find_area(cls, _area: Iterator, name: str, base_area: Any) -> float:
        cls.name = name
        for i_area in _area:
            cls.amount += i_area.find_area()
        if isinstance(base_area, int):
            cls.amount += base_area
        return cls.amount

    @property
    def area(self):
        return f'{self.name}: Площадь = {self.amount}'


class Cube(VolumetricMixin):
    """Класс, определяющий значения куба"""
    def __init__(self, name: Any, side: int = 4) -> None:
        self.size = [Square(name, side) for _ in range(6)]


class Pyramid(VolumetricMixin):
    """Класс, определяющий значения пирамиды"""
    def __init__(self, name: Any, h: int = 5, base: int = 8) -> None:
        self.size = [Triangle(name, h, base) for _ in range(4)]


triangle = Triangle('Треугольник', h=5, base=8)
square = Square('Квадрат', 4)

print(triangle.perimeter)
print(triangle.area)
print()
print(square.perimeter)
print(square.area)
print()

cube = Cube(None)
cube.find_area(cube.size, 'Куб', None)
print(cube.area)
pyramid = Pyramid(None)
pyramid.find_area(pyramid.size, 'Пирамида', triangle.base_area)
print(pyramid.area)
