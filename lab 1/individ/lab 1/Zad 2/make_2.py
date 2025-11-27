from zad_2 import Point


def main() -> None:
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


if __name__ == "__main__":
    main()
