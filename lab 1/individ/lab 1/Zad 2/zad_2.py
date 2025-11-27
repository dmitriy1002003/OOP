import math
from typing import Tuple


class Point:
    """
    first  — смещение точки по оси X
    second — смещение точки по оси Y
    """

    def __init__(self, first=0.0, second=0.0) -> None:
        """Проверка: оба аргумента должны быть числами."""
        try:
            self.first = float(first)
            self.second = float(second)
        except (TypeError, ValueError) as e:
            raise ValueError("Координаты должны быть числами.") from e

    def read(self) -> None:
        """Ввод координат с клавиатуры."""
        try:
            self.first = float(input("Введите смещение по оси X: "))
            self.second = float(input("Введите смещение по оси Y: "))
        except ValueError as e:
            raise ValueError("Координаты должны быть числами.") from e

    def display(self) -> None:
        """Вывод координат."""
        print(f"Координаты точки: ({self.first}, {self.second})")

    def distance_to_origin(self) -> float:
        """Расстояние от точки до начала координат."""
        return math.hypot(self.first, self.second)

    def distance_to(self, other: "Point") -> float:
        """Расстояние между двумя точками."""
        if not isinstance(other, Point):
            raise TypeError("Аргумент должен быть объектом Point.")
        dx = self.first - other.first
        dy = self.second - other.second
        return math.hypot(dx, dy)

    def to_polar(self) -> Tuple[float, float]:
        """Преобразование в полярные координаты (r, φ). φ в радианах."""
        r = math.hypot(self.first, self.second)
        phi = math.atan2(self.second, self.first)
        return r, phi

    def align_to(self, other: "Point") -> None:
        """Выравнивание: сделать текущую точку совпадающей с другой."""
        if not isinstance(other, Point):
            raise TypeError("Аргумент должен быть объектом Point.")
        self.first = other.first
        self.second = other.second

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.first == other.first and self.second == other.second

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f"Point({self.first}, {self.second})"


if __name__ == "__main__":
    p1 = Point(3.0, 4.0)
    p1.display()
    print("Расстояние до начала координат:", p1.distance_to_origin())

    p2 = Point(-1.0, 2.0)
    p2.display()
    print("Расстояние между p1 и p2:", p1.distance_to(p2))

    r, phi = p1.to_polar()
    print("Полярные координаты p1: r =", r, ", φ =", phi)

    print("Совпадают ли p1 и p2:", p1 == p2)
    p2.align_to(p1)
    print("После выравнивания p2.align_to(p1):")
    p2.display()
    print("Совпадают ли p1 и p2 теперь:", p1 == p2)

    print("\nВвод новой точки с клавиатуры:")
    p1.read()
    p1.display()
    print("Расстояние до начала координат:", p1.distance_to_origin())
    r, phi = p1.to_polar()
    print("Полярные координаты: r =", r, ", φ =", phi)
