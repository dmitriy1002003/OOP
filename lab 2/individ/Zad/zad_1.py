import math
from typing import Any, Iterator, Union


class Kalor:
    def __init__(self, first: int, second: float) -> None:
        try:
            first_int = int(first)
            second_float = float(second)
        except (ValueError, TypeError) as e:
            raise ValueError("Параметры должны быть числами.") from e
        if first_int <= 0 or second_float <= 0:
            raise ValueError("Параметры должны быть положительными.")
        self.first = first_int
        self.second = second_float

    def __str__(self) -> str:
        return f"Калорийность 100 г: {self.first} ккал, масса: {self.second} кг"

    def __repr__(self) -> str:
        return f"Kalor({self.first}, {self.second})"

    def power(self) -> float:
        return self.first * self.second * 10

    def Power(self) -> float:
        return self.power()

    def __abs__(self) -> float:
        return self.power()

    def __float__(self) -> float:
        return self.power()

    def __int__(self) -> int:
        return int(round(self.power()))

    def _total_kcal(self) -> float:
        return self.power()

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Kalor):
            return False
        return self.first == other.first and math.isclose(self.second, other.second)

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Kalor):
            return NotImplemented
        return self._total_kcal() < other._total_kcal()

    def __le__(self, other: Any) -> bool:
        if not isinstance(other, Kalor):
            return NotImplemented
        return self._total_kcal() <= other._total_kcal()

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Kalor):
            return NotImplemented
        return self._total_kcal() > other._total_kcal()

    def __ge__(self, other: Any) -> bool:
        if not isinstance(other, Kalor):
            return NotImplemented
        return self._total_kcal() >= other._total_kcal()

    def __add__(self, other: "Kalor") -> "Kalor":
        if not isinstance(other, Kalor):
            raise TypeError("Складывать можно только объекты Kalor.")
        total_mass = self.second + other.second
        total_kcal = self.power() + other.power()
        kcal_100g = total_kcal / (total_mass * 10)
        return Kalor(int(round(kcal_100g)), total_mass)

    def __sub__(self, other: "Kalor") -> "Kalor":
        if not isinstance(other, Kalor):
            raise TypeError("Вычитать можно только объекты Kalor.")
        new_first = self.first - other.first
        new_second = self.second - other.second
        if new_first <= 0 or new_second <= 0:
            raise ValueError("Результат вычитания привёл к неположительным значениям.")
        return Kalor(new_first, new_second)

    def __mul__(self, scalar: Union[int, float]) -> "Kalor":
        try:
            scalar_float = float(scalar)
        except (ValueError, TypeError):
            raise TypeError("Умножать можно только на число.")
        if scalar_float <= 0:
            raise ValueError("Множитель должен быть положительным.")
        new_mass = self.second * scalar_float
        return Kalor(self.first, new_mass)

    def __rmul__(self, scalar: Union[int, float]) -> "Kalor":
        return self.__mul__(scalar)

    def __truediv__(self, scalar: Union[int, float]) -> "Kalor":
        try:
            scalar_float = float(scalar)
        except (ValueError, TypeError):
            raise TypeError("Делить можно только на число.")
        if scalar_float <= 0:
            raise ValueError("Делитель должен быть положительным.")
        new_mass = self.second / scalar_float
        return Kalor(self.first, new_mass)

    def __iadd__(self, other: "Kalor") -> "Kalor":
        result = self + other
        self.first = result.first
        self.second = result.second
        return self

    def __isub__(self, other: "Kalor") -> "Kalor":
        result = self - other
        self.first = result.first
        self.second = result.second
        return self

    def __imul__(self, scalar: Union[int, float]) -> "Kalor":
        result = self * scalar
        self.first = result.first
        self.second = result.second
        return self

    def __itruediv__(self, scalar: Union[int, float]) -> "Kalor":
        result = self / scalar
        self.first = result.first
        self.second = result.second
        return self

    def __bool__(self) -> bool:
        return self.first > 0 and self.second > 0

    def __len__(self) -> int:
        return 2

    def __iter__(self) -> Iterator[float]:
        yield self.first
        yield self.second

    def read(self) -> None:
        while True:
            try:
                first = int(input("Введите калорийность 100 г продукта: "))
                second = float(input("Введите массу продукта в килограммах: "))
                if first <= 0 or second <= 0:
                    raise ValueError
                self.first = first
                self.second = second
                break
            except ValueError:
                print("Ошибка: введите корректные положительные числа.")

    def display(self) -> None:
        print(f"Калорийность 100 г: {self.first} ккал, масса продукта: {self.second} кг")

    def set_values(self, first: Union[int, float], second: Union[int, float]) -> None:
        obj = Kalor(first, second)
        self.first = obj.first
        self.second = obj.second


def make_Point(first: int, second: float) -> Kalor:
    try:
        obj = Kalor(first, second)
        return obj
    except ValueError as e:
        print("Ошибка при создании объекта Kalor:", e)
        raise SystemExit(1)


if __name__ == "__main__":
    k1 = make_Point(250, 0.35)
    k2 = make_Point(150, 0.5)

    k1.display()
    k2.display()

    print("power:", k1.power())
    print("Power:", k2.Power())
    print("abs(k1):", abs(k1))
    print("float(k1):", float(k1))
    print("int(k1):", int(k1))

    mix = k1 + k2
    print("k1 + k2:", mix)

    k3 = make_Point(300, 1.0)
    k4 = make_Point(100, 0.3)
    print("k3 - k4:", k3 - k4)

    print("k1 * 2:", k1 * 2)
    print("3 * k2:", 3 * k2)
    print("k2 / 2:", k2 / 2)

    k5 = make_Point(200, 0.2)
    k5 += k1
    k5 *= 2
    k5 /= 2
    print("k5 итог:", k5)

    print("k1 > k2:", k1 > k2)

    print("bool(k1):", bool(k1))

    print("len(k1):", len(k1))
    for v in k1:
        print(v)

    k_input = make_Point(100, 0.1)
    k_input.read()
    k_input.display()
    print(k_input.power())
