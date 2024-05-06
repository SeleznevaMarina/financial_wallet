import unittest
import os
from financial_wallet.wallet import Record, Wallet


class TestWallet(unittest.TestCase):
    """
    Класс для тестирования методов класса Wallet.

    Методы:
    - test_add_record(): Проверяет корректность добавления записи о доходе или расходе в кошелек.
    - test_search_records(): Проверяет корректность поиска записей о доходах и расходах в кошельке.
    """

    def test_add_record(self):
        wallet = Wallet("test_data.txt")
        record = Record("2022-05-01", "Доход", 1000.0, "Зарплата")
        wallet.add_record(record)
        self.assertEqual(len(wallet.records), 1)
        self.assertEqual(wallet.records[0].date, "2022-05-01")
        self.assertEqual(wallet.records[0].category, "Доход")
        self.assertEqual(wallet.records[0].amount, 1000.0)
        self.assertEqual(wallet.records[0].description, "Зарплата")

        if os.path.exists("test_data.txt"):
            os.remove("test_data.txt")

    def test_search_records(self):
        wallet = Wallet("test_data.txt")
        record1 = Record("2022-05-01", "Доход", 1000.0, "Зарплата")
        record2 = Record("2022-05-02", "Расход", 500.0, "Покупки")
        wallet.add_record(record1)
        wallet.add_record(record2)

        # Поиск по категории
        results_category = wallet.search_records(category="Доход")
        self.assertEqual(len(results_category), 1)
        self.assertEqual(results_category[0].category, "Доход")

        # Поиск по дате
        results_date = wallet.search_records(date="2022-05-02")
        self.assertEqual(len(results_date), 1)
        self.assertEqual(results_date[0].date, "2022-05-02")

        # Поиск по сумме
        results_amount = wallet.search_records(amount="500.0")
        self.assertEqual(len(results_amount), 1)
        self.assertEqual(results_amount[0].amount, 500.0)

        if os.path.exists("test_data.txt"):
            os.remove("test_data.txt")

    def test_edit_record(self):
        wallet = Wallet('test_data.txt')
        wallet.records = [
            Record("2022-05-01", "Доход", 1000.0, "Зарплата"),
            Record("2022-05-02", "Расход", 500.0, "Покупки")
        ]
        wallet.edit_record(0, Record("2022-05-01", "Доход", 2000.0, "Зарплата"))
        self.assertEqual(len(wallet.records), 2)
        self.assertEqual(wallet.records[0].date, "2022-05-01")
        self.assertEqual(wallet.records[0].category, "Доход")
        self.assertEqual(wallet.records[0].amount, 2000.0)
        self.assertEqual(wallet.records[0].description, "Зарплата")

        if os.path.exists("test_data.txt"):
            os.remove("test_data.txt")


if __name__ == "__main__":
    unittest.main()
