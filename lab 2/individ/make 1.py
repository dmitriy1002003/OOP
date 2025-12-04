from individ.Zad.zad_1 import Kalor


def main() -> None:
    k1 = Kalor(250, 0.35)
    k2 = Kalor(150, 0.5)

    print("Продукт 1:", k1)
    print("Продукт 2:", k2)
    print("Общая калорийность продукта 1:", k1.power())
    print("Модуль продукта 1 (abs):", abs(k1))

    print("\nАрифметические операции:")
    print("k1 + k2 =", k1 + k2)

    k_sub = Kalor(200, 0.5)
    k_sub2 = Kalor(100, 0.2)
    print("k_sub - k_sub2 =", k_sub - k_sub2)

    print("k1 * 2 =", k1 * 2)
    print("3 * k2 =", 3 * k2)
    print("k2 / 2 =", k2 / 2)

    k3 = Kalor(200, 0.2)
    k3 += k1
    print("k3 += k1 ->", k3)

    k3 *= 2
    print("k3 *= 2 ->", k3)

    print("\nСравнение:")
    print("k1 == k2:", k1 == k2)
    print("k1 != k2:", k1 != k2)
    print("k1 > k2:", k1 > k2)
    print("k1 < k2:", k1 < k2)

    print("\nБулева проверка:")
    print("k1 логически истинен:", bool(k1))

    print("\nИтерация по полям k1:")
    for value in k1:
        print("Значение:", value)


if __name__ == "__main__":
    main()
