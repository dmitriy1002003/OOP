from zad_1 import Kalor, make_Point

def main() -> None:
    """Демонстрация работы класса Kalor."""
    a = make_Point(300, 0.5)
    a.display()
    print("Общая калорийность продукта:", a.power(), "ккал")

    print("\nВвод значений с клавиатуры:")
    a.read()
    a.display()
    print("Общая калорийность продукта:", a.power(), "ккал")


if __name__ == "__main__":
    main()
