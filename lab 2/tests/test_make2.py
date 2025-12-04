import os
import sys
from datetime import datetime

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from individ.Zad.zad_2 import Goods, Receipt  # noqa: E402


class TestGoods:
    def test_initialization_with_string(self):
        goods = Goods("100,Яблоки,2.5,10")

        assert goods.get_code() == 100
        assert goods.get_name() == "Яблоки"
        assert goods.get_price() == 2.5
        assert goods.get_quantity() == 10

    def test_initialization_with_string_edge_cases(self):
        goods1 = Goods("999999,Товар,9999.99,9999")
        assert goods1.get_code() == 999999
        assert goods1.get_price() == 9999.99
        assert goods1.get_quantity() == 9999

        goods2 = Goods("0,, 0.0,0")
        assert goods2.get_code() == 0
        assert goods2.get_name() == ""
        assert goods2.get_price() == 0.0
        assert goods2.get_quantity() == 0

    def test_initialization_invalid_string(self):
        with pytest.raises(ValueError):
            Goods("100,Яблоки,2.5")

        with pytest.raises(ValueError):
            Goods("не число,Яблоки,2.5,10")

    def test_getters_setters(self):
        goods = Goods("100,Яблоки,2.5,10")

        assert goods.get_code() == 100
        assert goods.get_name() == "Яблоки"
        assert goods.get_price() == 2.5
        assert goods.get_quantity() == 10

        goods.set_code(200)
        goods.set_name("Бананы")
        goods.set_price(1.8)
        goods.set_quantity(15)

        assert goods.get_code() == 200
        assert goods.get_name() == "Бананы"
        assert goods.get_price() == 1.8
        assert goods.get_quantity() == 15

    def test_get_total(self):
        goods = Goods("100,Яблоки,2.5,10")
        assert goods.get_total() == 25.0

        goods_zero_price = Goods("101,Товар,0.0,10")
        assert goods_zero_price.get_total() == 0.0

        goods_zero_quantity = Goods("102,Товар,2.5,0")
        assert goods_zero_quantity.get_total() == 0.0

    def test_str_representation(self):
        goods = Goods("100,Яблоки,2.5,10")
        result = str(goods)

        assert "Товар [Код: 100" in result
        assert "Наименование: Яблоки" in result
        assert "Цена: 2.5" in result
        assert "Количество: 10" in result
        assert "Сумма: 25.0" in result


class TestReceipt:
    def test_initialization(self):
        receipt = Receipt(12345)

        assert receipt.get_receipt_number() == 12345
        assert receipt.size() == Receipt.MAX_SIZE
        assert receipt.get_count() == 0
        assert isinstance(receipt.get_date_time(), datetime)

    def test_initialization_custom_size(self):
        receipt = Receipt(12345, 50)

        assert receipt.get_receipt_number() == 12345
        assert receipt.size() == 50
        assert receipt.get_count() == 0

    def test_add_goods(self):
        receipt = Receipt(12345, 3)
        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("200,Бананы,1.8,15")

        assert receipt.add_goods(goods1) is True
        assert receipt.get_count() == 1

        assert receipt.add_goods(goods2) is True
        assert receipt.get_count() == 2

    def test_add_goods_max_capacity(self):
        receipt = Receipt(12345, 2)
        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("200,Бананы,1.8,15")
        goods3 = Goods("300,Апельсины,3.2,8")

        assert receipt.add_goods(goods1) is True
        assert receipt.add_goods(goods2) is True

        assert receipt.add_goods(goods3) is False
        assert receipt.get_count() == 2

    def test_update_goods(self):
        receipt = Receipt(12345)
        original_goods = Goods("100,Яблоки,2.5,10")
        updated_goods = Goods("100,Яблоки свежие,3.0,15")

        receipt.add_goods(original_goods)

        assert receipt.update_goods(updated_goods) is True

        found = receipt.find_goods_by_code(100)
        assert found.get_name() == "Яблоки свежие"
        assert found.get_price() == 3.0
        assert found.get_quantity() == 15

    def test_update_goods_not_found(self):
        receipt = Receipt(12345)
        goods = Goods("100,Яблоки,2.5,10")

        assert receipt.update_goods(goods) is False

    def test_remove_goods(self):
        receipt = Receipt(12345)
        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("200,Бананы,1.8,15")

        receipt.add_goods(goods1)
        receipt.add_goods(goods2)
        assert receipt.get_count() == 2

        assert receipt.remove_goods(100) is True
        assert receipt.get_count() == 1

        assert receipt.find_goods_by_code(100) is None
        assert receipt.find_goods_by_code(200) is not None

    def test_remove_goods_not_found(self):
        receipt = Receipt(12345)
        goods = Goods("100,Яблоки,2.5,10")
        receipt.add_goods(goods)

        assert receipt.remove_goods(999) is False
        assert receipt.get_count() == 1

    def test_find_goods_by_code(self):
        receipt = Receipt(12345)
        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("200,Бананы,1.8,15")

        receipt.add_goods(goods1)
        receipt.add_goods(goods2)

        found = receipt.find_goods_by_code(200)
        assert found is not None
        assert found.get_name() == "Бананы"

        not_found = receipt.find_goods_by_code(999)
        assert not_found is None

    def test_get_total_sum(self):
        receipt = Receipt(12345)
        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("200,Бананы,1.8,15")
        goods3 = Goods("300,Апельсины,3.2,8")

        receipt.add_goods(goods1)
        receipt.add_goods(goods2)
        receipt.add_goods(goods3)

        total = receipt.get_total_sum()
        expected_total = 25.0 + 27.0 + 25.6
        assert abs(total - expected_total) < 0.001

    def test_get_total_sum_empty_receipt(self):
        receipt = Receipt(12345)
        assert receipt.get_total_sum() == 0.0

    def test_indexing_operations(self):
        receipt = Receipt(12345)
        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("200,Бананы,1.8,15")

        receipt.add_goods(goods1)
        receipt.add_goods(goods2)

        assert receipt[0].get_code() == 100
        assert receipt[1].get_code() == 200

        new_goods = Goods("300,Груши,2.8,12")
        receipt[1] = new_goods
        assert receipt[1].get_code() == 300

    def test_indexing_out_of_range(self):
        receipt = Receipt(12345)

        with pytest.raises(IndexError):
            _ = receipt[0]

        goods = Goods("100,Яблоки,2.5,10")
        receipt.add_goods(goods)

        with pytest.raises(IndexError):
            _ = receipt[1]

        with pytest.raises(IndexError):
            _ = receipt[-1]

    def test_length_method(self):
        receipt = Receipt(12345)

        assert len(receipt) == 0

        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("200,Бананы,1.8,15")

        receipt.add_goods(goods1)
        assert len(receipt) == 1

        receipt.add_goods(goods2)
        assert len(receipt) == 2

    def test_str_representation(self):
        receipt = Receipt(12345)
        goods = Goods("100,Яблоки,2.5,10")
        receipt.add_goods(goods)

        result = str(receipt)

        assert "Товарный чек №12345" in result
        assert "Товаров: 1/100" in result
        assert "Яблоки" in result
        assert "Общая сумма: 25.00" in result

    def test_str_representation_empty(self):
        receipt = Receipt(12345)
        result = str(receipt)

        assert "Товарный чек №12345" in result
        assert "Товаров: 0/100" in result
        assert "Общая сумма: 0.00" in result


class TestReceiptIntegration:
    def test_complete_workflow(self):
        receipt = Receipt(12345, 5)

        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("200,Бананы,1.8,15")
        goods3 = Goods("300,Апельсины,3.2,8")

        assert receipt.add_goods(goods1) is True
        assert receipt.add_goods(goods2) is True
        assert receipt.add_goods(goods3) is True
        assert receipt.get_count() == 3

        total = receipt.get_total_sum()
        expected = 2.5 * 10 + 1.8 * 15 + 3.2 * 8
        assert abs(total - expected) < 0.001

        updated_goods = Goods("200,Бананы спелые,2.0,20")
        assert receipt.update_goods(updated_goods) is True

        updated_total = receipt.get_total_sum()
        updated_expected = 2.5 * 10 + 2.0 * 20 + 3.2 * 8
        assert abs(updated_total - updated_expected) < 0.001

        assert receipt.remove_goods(100) is True
        assert receipt.get_count() == 2

        final_total = receipt.get_total_sum()
        final_expected = 2.0 * 20 + 3.2 * 8
        assert abs(final_total - final_expected) < 0.001

        assert receipt[0].get_code() == 200
        assert receipt[1].get_code() == 300

    def test_multiple_operations_on_same_receipt(self):
        receipt = Receipt(99999, 10)

        for i in range(5):
            goods = Goods(f"{i+100},Товар{i+1},{1.0 + i*0.5},{5 + i}")
            receipt.add_goods(goods)

        assert receipt.get_count() == 5
        assert len(receipt) == 5

        updated_goods = Goods("102,ТоварОбновленный,5.0,20")
        receipt.update_goods(updated_goods)

        receipt.remove_goods(101)

        assert receipt.get_count() == 4
        assert receipt.find_goods_by_code(101) is None
        assert receipt.find_goods_by_code(102).get_price() == 5.0


class TestEdgeCases:
    def test_receipt_with_zero_size(self):
        receipt = Receipt(12345, 0)
        goods = Goods("100,Яблоки,2.5,10")

        assert receipt.add_goods(goods) is False
        assert receipt.get_count() == 0

    def test_duplicate_goods_codes(self):
        receipt = Receipt(12345)
        goods1 = Goods("100,Яблоки,2.5,10")
        goods2 = Goods("100,Бананы,1.8,15")

        receipt.add_goods(goods1)
        receipt.add_goods(goods2)

        assert receipt.get_count() == 2
        assert receipt[0].get_code() == 100
        assert receipt[1].get_code() == 100


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
