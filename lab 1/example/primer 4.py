from typing import Optional


class Rational:
    def __init__(self, a: int = 0, b: int = 1) -> None:
        a = int(a)
        b = int(b)

        if b == 0:
            raise ValueError("Denominator cannot be zero")

        # Обработка дроби
        if b < 0:
            a = -a
            b = -b

        self.__numerator = a
        self.__denominator = b
        self.__reduce()

    # Сокращение дроби
    def __reduce(self) -> None:
        # Функция для нахождения наибольшего общего делителя
        def gcd(a: int, b: int) -> int:
            if a == 0:
                return b
            elif b == 0:
                return a
            elif a >= b:
                return gcd(a % b, b)
            else:
                return gcd(a, b % a)

        c = gcd(abs(self.__numerator), abs(self.__denominator))
        self.__numerator //= c
        self.__denominator //= c

    @property
    def numerator(self) -> int:
        return self.__numerator

    @property
    def denominator(self) -> int:
        return self.__denominator

    # Прочитать значение дроби с клавиатуры
    def read(self, prompt: Optional[str] = None) -> None:
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split("/", maxsplit=1)))

        if parts[1] == 0:
            raise ValueError("Denominator cannot be zero")

        # Обработка знака дроби
        if parts[1] < 0:
            parts[0] = -parts[0]
            parts[1] = -parts[1]

        self.__numerator = parts[0]
        self.__denominator = parts[1]
        self.__reduce()

    # Вывести дробь на экран
    def display(self) -> None:
        print(f"{self.__numerator}/{self.__denominator}")

    # Сложение обыкновенных дробей
    def add(self, rhs: "Rational") -> "Rational":
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator + self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Argument must be a Rational number")

    # Вычитание обыкновенных дробей
    def sub(self, rhs: "Rational") -> "Rational":
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator - self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Argument must be a Rational number")

    # Умножение обыкновенных дробей
    def mul(self, rhs: "Rational") -> "Rational":
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.numerator
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Argument must be a Rational number")

    # Деление обыкновенных дробей
    def div(self, rhs: "Rational") -> "Rational":
        if isinstance(rhs, Rational):
            if rhs.numerator == 0:
                raise ValueError("Cannot divide by zero")
            a = self.numerator * rhs.denominator
            b = self.denominator * rhs.numerator
            return Rational(a, b)
        else:
            raise ValueError("Argument must be a Rational number")

    # Проверка на равенство
    def equals(self, rhs: object) -> bool:
        if isinstance(rhs, Rational):
            return (self.numerator == rhs.numerator) and (
                self.denominator == rhs.denominator
            )
        else:
            return False

    # Проверка на больше
    def greater(self, rhs: object) -> bool:
        if isinstance(rhs, Rational):
            # Сравнение без потери точности
            return self.numerator * rhs.denominator > rhs.numerator * self.denominator
        else:
            return False

    # Проверка на меньше
    def less(self, rhs: object) -> bool:
        if isinstance(rhs, Rational):
            # Сравнение без потери точности
            return self.numerator * rhs.denominator < rhs.numerator * self.denominator
        else:
            return False


if __name__ == "__main__":
    r1 = Rational(3, 4)
    r1.display()

    r2 = Rational()
    r2.read("Введите обыкновенную дробь: ")
    r2.display()

    r3 = r2.add(r1)
    r3.display()

    r4 = r2.sub(r1)
    r4.display()

    r5 = r2.mul(r1)
    r5.display()

    r6 = r2.div(r1)
    r6.display()
