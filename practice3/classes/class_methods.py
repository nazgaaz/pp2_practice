# 1) метод печатает приветствие
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello, my name is " + self.name)
Person("Emil").greet()


# 2) метод меняет состояние
class Person:
    def __init__(self, age):
        self.age = age
    def birthday(self):
        self.age += 1
p = Person(25); p.birthday(); print(p.age)

# 3) метод возвращает значение
class Calc:
    def add(self, a, b):
        return a + b
print(Calc().add(2, 3))


# 4) метод использует self
class Car:
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(self.brand)
Car("Ford").show()

# 5) __str__ как “метод для print”
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
print(Person("Linus"))


