# 1) наследник меняет поведение
class Animal:
    def speak(self):
        print("...")
class Dog(Animal):
    def speak(self):
        print("Woof")
Dog().speak()


# 2) можно всё равно вызвать родителя через super()
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")
Dog().speak()


# 3) одинаковое имя метода в разных классах (полиморфизм-идея)
class Car:
    def move(self): print("Drive")
class Boat:
    def move(self): print("Sail")
for v in (Car(), Boat()):
    v.move()


# 4) переопределение + использование полей
class Person:
    def __init__(self, name): self.name = name
    def show(self): print(self.name)

class Student(Person):
    def show(self): print("Student:", self.name)
Student("Emil").show()


# 5) переопределение “родительского” метода из примеров наследования
class Parent:
    def welcome(self): print("Welcome (parent)")
class Child(Parent):
    def welcome(self): print("Welcome (child)")
Child().welcome()
