import math


class Kalor:
    """
    first  — калорийность 100 г продукта (целое положительное число, ккал)
    second — масса продукта в килограммах (дробное положительное число)
    """

    def __init__(self, first: int, second: float) -> None:
        try:
            first = int(first)
            second = float(second)
        except (ValueError, TypeError) as e:
            raise ValueError("Параметры должны быть числами.") from e

        if first <= 0 or second <= 0:
            raise ValueError("Параметры должны быть положительными.")

        self.first = first
        self.second = second

    def read(self) -> None:
        """Ввод значений с клавиатуры с контролем корректности."""
        while True:
            try:
                first = int(input(
                    "Введите калорийность 100 г продукта "
                    "(целое положительное число, ккал): "
                ))
                second = float(input(
                    "Введите массу продукта в килограммах "
                    "(дробное положительное число): "
                ))
                if first <= 0 or second <= 0:
                    raise ValueError
                self.first = first
                self.second = second
                break
            except ValueError:
                print("Ошибка: введите корректные положительные числа.")

    def display(self) -> None:
        """Вывод значений полей."""
        print(
            f"Калорийность 100 г: {self.first} ккал, "
            f"масса продукта: {self.second} кг"
        )

    def power(self) -> float:
        """
        Вычисление общей калорийности продукта.

        Формула:
        количество порций по 100 г = масса_кг * 10
        общая калорийность = калорийность_100г * масса_кг * 10
        """
        return self.first * self.second * 10

    # Заглавная буква
    def Power(self) -> float:
        return self.power()


def make_Point(first: int, second: float) -> Kalor:
    """
    Внешняя функция для создания объекта Kalor.

    При ошибке выводит сообщение и завершает работу программы.
    """
    try:
        obj = Kalor(first, second)
        return obj
    except ValueError as e:
        print("Ошибка при создании объекта Kalor:", e)
        raise SystemExit(1)


if __name__ == "__main__":
    k1 = make_Point(250, 0.35)
    k1.display()
    print("Общая калорийность продукта:", k1.power(), "ккал")

    print("\nВвод новых значений с клавиатуры:")
    k1.read()
    k1.display()
    print("Общая калорийность продукта:", k1.Power(), "ккал")
