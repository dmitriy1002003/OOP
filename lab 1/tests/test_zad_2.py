import math
import os
import sys
from typing import Any

import pytest

BASE_DIR = os.path.dirname(__file__)
ZAD2_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..", "individ", "lab 1", "Zad 2")
)
sys.path.insert(0, ZAD2_DIR)

from zad_2 import Point


class TestPoint:
    def test_initialization_default(self) -> None:
        p = Point()
        assert p.first == 0.0
        assert p.second == 0.0

    def test_initialization_with_values(self) -> None:
        p = Point(3.5, -4.2)
        assert p.first == 3.5
        assert p.second == -4.2

    def test_initialization_with_ints(self) -> None:
        p = Point(3, 4)
        assert p.first == 3.0
        assert p.second == 4.0

    def test_initialization_invalid(self) -> None:
        with pytest.raises(ValueError):
            Point("a", "b")  # type: ignore

    def test_distance_to_origin(self) -> None:
        p = Point(3.0, 4.0)
        assert p.distance_to_origin() == pytest.approx(5.0)

    def test_distance_between_points(self) -> None:
        p1 = Point(1.0, 1.0)
        p2 = Point(4.0, 5.0)
        assert p1.distance_to(p2) == pytest.approx(5.0)

    def test_to_polar(self) -> None:
        p = Point(1.0, math.sqrt(3.0))
        r, phi = p.to_polar()
        assert r == pytest.approx(2.0)
        assert phi == pytest.approx(math.pi / 3, rel=1e-6)

    def test_align_to(self) -> None:
        p1 = Point(2.0, 3.0)
        p2 = Point(-1.0, -5.0)
        p2.align_to(p1)
        assert p2.first == p1.first
        assert p2.second == p1.second
        assert p1 == p2

    def test_equality_and_inequality(self) -> None:
        p1 = Point(1.0, 2.0)
        p2 = Point(1.0, 2.0)
        p3 = Point(2.0, 3.0)
        assert p1 == p2
        assert p1 != p3

    def test_display(self, capsys: Any) -> None:
        p = Point(1.5, 2.5)
        p.display()
        captured = capsys.readouterr()
        assert "(1.5, 2.5)" in captured.out


class TestPointEdgeCases:
    def test_large_numbers(self) -> None:
        p = Point(1_000_000.0, -1_000_000.0)
        r = p.distance_to_origin()
        expected = math.sqrt(2_000_000_000_000.0)
        assert math.isclose(r, expected)

    def test_float_precision(self) -> None:
        p = Point(0.1, 0.2)
        r = p.distance_to_origin()
        expected = math.sqrt(0.01 + 0.04)
        assert math.isclose(r, expected)
