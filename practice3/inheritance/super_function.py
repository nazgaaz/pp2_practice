# 1) super() вызывает __init__ родителя
class Person:
    def __init__(self, fname):
        self.fname = fname

class Student(Person):
    def __init__(self, fname):
        super().__init__(fname)

print(Student("Emil").fname)


# 2) super() + новое поле
class Student(Person):
    def __init__(self, fname, year):
        super().__init__(fname)
        self.year = year
print(Student("Emil", 2026).year)


# 3) super() может вызывать методы родителя
class Person:
    def hello(self):
        print("Hello")

class Student(Person):
    def hello(self):
        super().hello()
        print("from Student")
Student().hello()


# 4) super() без аргументов (обычно так и пишут)
class A:
    def f(self): print("A")
class B(A):
    def f(self):
        super().f()
B().f()


# 5) super() как “доступ к родительскому поведению”
class Parent:
    def info(self): return "Parent"
class Child(Parent):
    def info(self): return super().info() + " + Child"
print(Child().info())
