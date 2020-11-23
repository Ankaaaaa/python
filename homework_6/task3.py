class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print('доход сотрудника составляет', sum(self._income.values()))




worker = Position('Вася', 'Петров', 'директор', {"wage": 100, "bonus": 50})
print(worker.position)
worker.get_full_name()
worker.get_total_income()