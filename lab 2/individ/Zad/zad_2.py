from decimal import Decimal, getcontext


class Fraction:
    MAX_SIZE = 100

    def __init__(self, value: str, size: int | None = None):
        s = value.strip()
        if not s:
            raise ValueError("Строка числа пуста")
        if s[0] == "+":
            s = s[1:]
        if "-" in s:
            raise ValueError("Число должно быть беззнаковым")
        if s.count(".") > 1:
            raise ValueError("Неверный формат числа")

        if "." in s:
            int_str, frac_str = s.split(".")
        else:
            int_str, frac_str = s, ""

        if not int_str:
            int_str = "0"
        if not int_str.isdigit() or (frac_str and not frac_str.isdigit()):
            raise ValueError("Строка должна содержать только цифры и точку")

        int_str = int_str.lstrip("0") or "0"
        frac_str = frac_str.rstrip("0")

        int_digits = [int(ch) for ch in reversed(int_str)]
        frac_digits = [int(ch) for ch in frac_str] if frac_str else []

        count = len(int_digits) + len(frac_digits)
        if count == 0:
            int_digits = [0]
            count = 1

        if size is None:
            size_val = count
        else:
            size_val = int(size)
            if size_val <= 0:
                raise ValueError("size должен быть положительным")
            if count > size_val:
                raise ValueError("Количество цифр превышает size")

        if count > Fraction.MAX_SIZE:
            raise ValueError("Превышен максимальный размер Fraction")

        self.int_part = int_digits
        self.frac_part = frac_digits
        self._size = size_val
        self.count = count

    def _to_string(self) -> str:
        int_str = "".join(str(d) for d in reversed(self.int_part)).lstrip("0") or "0"
        if self.frac_part:
            frac_str = "".join(str(d) for d in self.frac_part).rstrip("0")
            if frac_str:
                return int_str + "." + frac_str
        return int_str

    @staticmethod
    def _normalize_decimal_string(s: str) -> str:
        s = s.strip()
        if "." in s:
            int_str, frac_str = s.split(".")
            frac_str = frac_str.rstrip("0")
            int_str = int_str.lstrip("0") or "0"
            if frac_str:
                return int_str + "." + frac_str
            return int_str
        return s.lstrip("0") or "0"

    @classmethod
    def from_decimal(cls, dec: Decimal) -> "Fraction":
        getcontext().prec = cls.MAX_SIZE
        s = format(dec, "f")
        s = cls._normalize_decimal_string(s)
        return cls(s)

    def __str__(self) -> str:
        return self._to_string()

    def __repr__(self) -> str:
        return f"Fraction('{self._to_string()}', size={self._size})"

    def to_decimal(self) -> Decimal:
        getcontext().prec = Fraction.MAX_SIZE
        return Decimal(self._to_string())

    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self.count

    def __getitem__(self, index: int) -> int:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= self.count:
            raise IndexError("Индекс вне диапазона")
        if index < len(self.int_part):
            return self.int_part[index]
        j = index - len(self.int_part)
        return self.frac_part[j]

    def __setitem__(self, index: int, value: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if not isinstance(value, int) or not (0 <= value <= 9):
            raise ValueError("Значение должно быть цифрой 0..9")
        if index < 0 or index >= self.count:
            raise IndexError("Индекс вне диапазона")
        if index < len(self.int_part):
            self.int_part[index] = value
        else:
            j = index - len(self.int_part)
            self.frac_part[j] = value

    def __iter__(self):
        for d in self.int_part:
            yield d
        for d in self.frac_part:
            yield d

    def __bool__(self) -> bool:
        return any(self.int_part) or any(self.frac_part)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.to_decimal() == other.to_decimal()

    def __lt__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.to_decimal() < other.to_decimal()

    def __le__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.to_decimal() <= other.to_decimal()

    def __gt__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.to_decimal() > other.to_decimal()

    def __ge__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.to_decimal() >= other.to_decimal()

    def __add__(self, other) -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented
        res = self.to_decimal() + other.to_decimal()
        if res < 0:
            raise ValueError("Результат сложения отрицателен")
        return Fraction.from_decimal(res)

    def __sub__(self, other) -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented
        res = self.to_decimal() - other.to_decimal()
        if res < 0:
            raise ValueError("Результат вычитания отрицателен")
        return Fraction.from_decimal(res)

    def __mul__(self, other) -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented
        res = self.to_decimal() * other.to_decimal()
        if res < 0:
            raise ValueError("Результат умножения отрицателен")
        return Fraction.from_decimal(res)


if __name__ == "__main__":
    a = Fraction("123.45")
    b = Fraction("7.005")
    print("a =", a)
    print("b =", b)
    print("size(a) =", a.size())
    print("len(a) =", len(a))
    print("count(a) =", a.count)

    print("a[0] (младшая цифра целой части):", a[0])
    print("a[1]:", a[1])
    print("a[2]:", a[2])

    idx_frac = len(a.int_part)
    print("a[индекс первой дробной цифры]:", a[idx_frac])

    a[0] = 9
    print("a после изменения младшей целой цифры:", a)

    c = a + b
    d = a - Fraction("23.45")
    e = a * b

    print("a + b =", c)
    print("a - 23.45 =", d)
    print("a * b =", e)

    print("a == b:", a == b)
    print("a > b:", a > b)
    print("a < b:", a < b)

    print("Итерация по цифрам a:")
    for digit in a:
        print(digit, end=" ")
    print()
