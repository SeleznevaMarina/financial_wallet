class Record:
    """
    Класс для представления записей о доходе или расходе в кошельке.

    Атрибуты:
    - date (str): Дата записи.
    - category (str): Категория записи (Доход/Расход).
    - amount (float): Сумма записи.
    - description (str): Описание записи.
    """

    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"Дата: {self.date}, Категория: {self.category}, Сумма: {self.amount}, Описание: {self.description}"

class Wallet:
    """
    Класс для управления кошельком с записями о доходах и расходах.

    Атрибуты:
    - filename (str): Имя файла для хранения данных.
    - records (List[Record]): Список объектов класса Record.
    """
    
    def __init__(self, filename):
        self.filename = filename
        self.records = []
        self.load_records()

    def load_records(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read().strip().split("\n\n")
                for entry in data:
                    lines = entry.strip().split("\n")
                    date = lines[0].split(": ")[1]
                    category = lines[1].split(": ")[1]
                    amount = float(lines[2].split(": ")[1])
                    description = lines[3].split(": ")[1]
                    record = Record(date, category, amount, description)
                    self.records.append(record)
        except FileNotFoundError:
            print("Файл с данными не найден.")

    def save_records(self):
        with open(self.filename, "w") as file:
            for record in self.records:
                file.write(f"Дата: {record.date}\n")
                file.write(f"Категория: {record.category}\n")
                file.write(f"Сумма: {record.amount}\n")
                file.write(f"Описание: {record.description}\n")
                file.write("\n")

    def add_record(self, record):
        self.records.append(record)
        self.save_records()

    def edit_record(self, index, new_record):
        self.records[index] = new_record
        self.save_records()

    def search_records(self, category=None, date=None, amount=None):
        results = []
        for record in self.records:
            if (not category or record.category.lower() == category.lower()) and \
               (not date or record.date == date) and \
               (not amount or record.amount == float(amount)):
                results.append(record)
        return results

    def calculate_balance(self):
        income = sum(record.amount for record in self.records if record.category.lower() == "доход")
        expense = sum(record.amount for record in self.records if record.category.lower() == "расход")
        return {"income": income, "expense": expense, "total": income - expense}
