class Record:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"Дата: {self.date}, Категория: {self.category}, Сумма: {self.amount}, Описание: {self.description}"

class Wallet:
    def __init__(self, filename):
        self.filename = filename
        self.records = []
        self.load_records()

    def load_records(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split("\n")
                    date = data[0].split(": ")[1]
                    category = data[1].split(": ")[1]
                    amount = float(data[2].split(": ")[1])
                    description = data[3].split(": ")[1]
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
