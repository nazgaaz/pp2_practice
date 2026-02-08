# 1) наследование методов
class Person:
    def __init__(self, name):
        self.name = name
    def printname(self):
        print(self.name)

class Student(Person):
    pass

Student("Emil").printname()


# 2) свой метод в наследнике
class Student(Person):
    def welcome(self):
        print("Welcome", self.name)
Student("Linus").welcome()


# 3) свой __init__ (без super) — через имя родителя
class Student(Person):
    def __init__(self, name):
        Person.__init__(self, name)


# 4) добавить новое поле
class Student(Person):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year


# 5) наследник может “переопределить” метод
class Student(Person):
    def printname(self):
        print("Student:", self.name)
