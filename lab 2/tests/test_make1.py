import math
import os
import sys
from io import StringIO
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from individ.Zad.zad_1 import Kalor, make_Point  # noqa: E402


class TestKalor:
    def test_initialization_valid(self):
        k = Kalor(250, 0.35)
        assert k.first == 250
        assert math.isclose(k.second, 0.35)

    def test_initialization_invalid_type(self):
        with pytest.raises(ValueError, match="Параметры должны быть числами."):
            Kalor("invalid", "values")

    def test_initialization_non_positive(self):
        with pytest.raises(ValueError, match="Параметры должны быть положительными."):
            Kalor(0, 0.1)
        with pytest.raises(ValueError, match="Параметры должны быть положительными."):
            Kalor(100, -0.5)

    def test_str_representation(self):
        k = Kalor(250, 0.35)
        assert str(k) == "Калорийность 100 г: 250 ккал, масса: 0.35 кг"

    def test_repr_representation(self):
        k = Kalor(250, 0.35)
        assert repr(k) == "Kalor(250, 0.35)"

    def test_power_and_Power(self):
        k = Kalor(200, 0.5)
        assert math.isclose(k.power(), 200 * 0.5 * 10)
        assert math.isclose(k.Power(), 200 * 0.5 * 10)

    def test_abs_float_int_conversion(self):
        k = Kalor(150, 0.4)
        total = 150 * 0.4 * 10
        assert math.isclose(abs(k), total)
        assert math.isclose(float(k), total)
        assert int(k) == int(round(total))

    def test_addition(self):
        k1 = Kalor(200, 0.5)   # 1000 ккал
        k2 = Kalor(100, 0.5)   # 500 ккал
        res = k1 + k2          # масса 1.0, всего 1500 ккал

        assert isinstance(res, Kalor)
        assert res.first == 150
        assert math.isclose(res.second, 1.0)
        assert math.isclose(res.power(), k1.power() + k2.power())

    def test_addition_invalid_type(self):
        k = Kalor(200, 0.5)
        with pytest.raises(TypeError, match="Складывать можно только объекты Kalor."):
            _ = k + "invalid"

    def test_subtraction(self):
        k1 = Kalor(300, 1.0)
        k2 = Kalor(100, 0.3)
        res = k1 - k2
        assert res.first == 200
        assert math.isclose(res.second, 0.7)

    def test_subtraction_to_non_positive_raises(self):
        k1 = Kalor(100, 0.5)
        k2 = Kalor(150, 0.6)
        with pytest.raises(
            ValueError, match="Результат вычитания привёл к неположительным значениям."
        ):
            _ = k1 - k2

    def test_subtraction_invalid_type(self):
        k = Kalor(200, 0.5)
        with pytest.raises(TypeError, match="Вычитать можно только объекты Kalor."):
            _ = k - 10

    def test_multiplication(self):
        k = Kalor(250, 0.4)
        res = k * 2
        assert res.first == 250
        assert math.isclose(res.second, 0.8)

    def test_right_multiplication(self):
        k = Kalor(250, 0.4)
        res = 3 * k
        assert res.first == 250
        assert math.isclose(res.second, 1.2)

    def test_multiplication_invalid_type(self):
        k = Kalor(250, 0.4)
        with pytest.raises(TypeError, match="Умножать можно только на число."):
            _ = k * "x"

    def test_multiplication_non_positive_scalar(self):
        k = Kalor(250, 0.4)
        with pytest.raises(ValueError, match="Множитель должен быть положительным."):
            _ = k * 0
        with pytest.raises(ValueError, match="Множитель должен быть положительным."):
            _ = k * -1

    def test_division(self):
        k = Kalor(250, 0.8)
        res = k / 2
        assert res.first == 250
        assert math.isclose(res.second, 0.4)

    def test_division_invalid_type(self):
        k = Kalor(250, 0.8)
        with pytest.raises(TypeError, match="Делить можно только на число."):
            _ = k / "x"

    def test_division_non_positive_scalar(self):
        k = Kalor(250, 0.8)
        with pytest.raises(ValueError, match="Делитель должен быть положительным."):
            _ = k / 0
        with pytest.raises(ValueError, match="Делитель должен быть положительным."):
            _ = k / -1

    def test_inplace_addition(self):
        k1 = Kalor(200, 0.5)
        k2 = Kalor(100, 0.3)
        k1 += k2
        assert isinstance(k1, Kalor)
        assert math.isclose(k1.power(), Kalor(150, 0.8).power())

    def test_inplace_subtraction(self):
        k1 = Kalor(300, 1.0)
        k2 = Kalor(100, 0.3)
        k1 -= k2
        assert k1.first == 200
        assert math.isclose(k1.second, 0.7)

    def test_inplace_multiplication(self):
        k = Kalor(250, 0.4)
        k *= 2
        assert k.first == 250
        assert math.isclose(k.second, 0.8)

    def test_inplace_division(self):
        k = Kalor(250, 0.8)
        k /= 2
        assert k.first == 250
        assert math.isclose(k.second, 0.4)

    def test_comparison_by_total_kcal(self):
        k1 = Kalor(200, 0.5)  # 1000
        k2 = Kalor(100, 0.5)  # 500
        k3 = Kalor(200, 0.5)

        assert k1 > k2
        assert k2 < k1
        assert k1 >= k3
        assert k1 <= k3
        assert k1 == k3
        assert k1 != k2

    def test_equality_with_other_type(self):
        k = Kalor(200, 0.5)
        assert (k == "x") is False
        assert (k != "x") is True

    def test_bool_conversion(self):
        k = Kalor(200, 0.5)
        assert bool(k) is True

    def test_len(self):
        k = Kalor(200, 0.5)
        assert len(k) == 2

    def test_iteration(self):
        k = Kalor(250, 0.35)
        values = list(k)
        assert values[0] == 250
        assert math.isclose(values[1], 0.35)
        assert len(values) == 2

    @patch("sys.stdout", new_callable=StringIO)
    def test_display(self, mock_stdout):
        k = Kalor(250, 0.35)
        k.display()
        out = mock_stdout.getvalue()
        assert "Калорийность 100 г: 250 ккал, масса продукта: 0.35 кг" in out

    @patch("builtins.input", side_effect=["300", "0.5"])
    def test_read(self, mock_input):
        k = Kalor(100, 0.1)
        k.read()
        assert k.first == 300
        assert math.isclose(k.second, 0.5)

    def test_set_values(self):
        k = Kalor(100, 0.1)
        k.set_values(200, 0.4)
        assert k.first == 200
        assert math.isclose(k.second, 0.4)

    def test_set_values_invalid(self):
        k = Kalor(100, 0.1)
        with pytest.raises(ValueError, match="Параметры должны быть числами."):
            k.set_values("x", 0.3)


class TestMakePoint:
    def test_make_point_valid(self):
        k = make_Point(250, 0.35)
        assert isinstance(k, Kalor)
        assert k.first == 250
        assert math.isclose(k.second, 0.35)

    def test_make_point_invalid(self):
        with pytest.raises(SystemExit):
            _ = make_Point("x", 0.3)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
