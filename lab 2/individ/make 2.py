from individ.Zad.zad_2 import Goods, Receipt


def main() -> None:
    receipt = Receipt(12345, size=5)

    goods1 = Goods("100,Яблоки,2.5,10")
    goods2 = Goods("200,Бананы,1.8,15")
    goods3 = Goods("300,Люди,3.2,8")

    receipt.add_goods(goods1)
    receipt.add_goods(goods2)
    receipt.add_goods(goods3)

    print("Исходный чек:")
    print(receipt)
    print("\n" + "=" * 50)

    print("\nДоступ через индексирование:")
    for i in range(len(receipt)):
        print(f"receipt[{i}] = {receipt[i]}")

    print("\nИзменение через индексирование:")
    receipt[1] = Goods("250,Груши,2.8,12")
    print(f"После изменения: {receipt[1]}")

    print("\nПоиск товара с кодом 100:")
    found = receipt.find_goods_by_code(100)
    print(found if found else "Не найден")

    print(f"\nОбщая сумма чека: {receipt.get_total_sum():.2f}")


if __name__ == "__main__":
    main()
