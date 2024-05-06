from wallet import Wallet, Record

class App:
    """
    Класс для консольного приложения "Личный финансовый кошелек".

    Атрибуты:
    - wallet (Wallet): Объект класса Wallet для управления кошельком.
    """

    def __init__(self):
        self.wallet = Wallet("data.txt")

    def run(self):
        while True:
            print("\nЛичный финансовый кошелек")
            print("1. Вывод баланса")
            print("2. Добавление записи")
            print("3. Редактирование записи")
            print("4. Поиск по записям")
            print("5. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.show_balance()
            elif choice == "2":
                self.add_record()
            elif choice == "3":
                self.edit_record()
            elif choice == "4":
                self.search_records()
            elif choice == "5":
                print("\nВыход из программы.")
                break
            else:
                print("\nНекорректный выбор.")

    def show_balance(self):
        balance = self.wallet.calculate_balance()
        print(f"\nТекущий баланс: {balance['total']}")
        print(f"Доходы: {balance['income']}")
        print(f"Расходы: {balance['expense']}")

    def add_record(self):
        date = input("Введите дату (гггг-мм-дд): ")
        category = input("Введите категорию (Доход/Расход): ")
        amount = float(input("Введите сумму: "))
        description = input("Введите описание: ")
        record = Record(date, category, amount, description)
        self.wallet.add_record(record)
        print("Запись успешно добавлена.")

    def edit_record(self):
        index = int(input("Введите номер записи для редактирования: "))
        if index < 1 or index > len(self.wallet.records):
            print("\nНекорректный номер записи.")
            return
        date = input("Введите новую дату (гггг-мм-дд): ")
        category = input("Введите новую категорию (Доход/Расход): ")
        amount = float(input("Введите новую сумму: "))
        description = input("Введите новое описание: ")
        new_record = {"date": date, "category": category, "amount": amount, "description": description}
        self.wallet.edit_record(index - 1, new_record)
        print("\nЗапись успешно отредактирована.")

    def search_records(self):
        print("Выберите параметры для поиска:")
        category = input("Категория (Доход/Расход): ")
        date = input("Дата (гггг-мм-дд): ")
        amount = input("Сумма: ")
        results = self.wallet.search_records(category, date, amount)
        if results:
            print("\nРезультаты поиска:")
            for i, record in enumerate(results, 1):
                print(f"{i}. {record}")
        else:
            print("\nЗаписи не найдены.")

if __name__ == "__main__":
    app = App()
    app.run()
