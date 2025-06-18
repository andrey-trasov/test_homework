

class Employee:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"Имя {self.name}, должность {self.position}, зарплата {self.salary}"


class Developer(Employee):

    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        return f"Имя {self.name}, должность {self.position}, зарплата {self.salary}, язык програмирования {self.programming_language}"



class Manager(Employee):

    def __init__(self, name, position, salary, employees):
        super().__init__(name, position, salary)
        self.employees = employees

    def get_info(self):
        return f"Имя {self.name}, должность {self.position}, зарплата {self.salary}, список подчинённых {self.employees}"


developer = Developer("андрей", "мидл", 100, "python")
print(developer.get_info())


manager = Manager("андрей", "мидл", 100, ['QWE', "WEF"])
print(manager.get_info())