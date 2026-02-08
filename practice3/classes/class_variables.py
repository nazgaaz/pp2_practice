# 1) общий атрибут класса
class MyClass:
    x = 5
print(MyClass.x)


# 2) доступ через объект
class MyClass:
    x = 5
p = MyClass()
print(p.x)


# 3) изменение атрибута класса влияет на новые/все обращения
class A:
    x = 1
A.x = 99
print(A().x)


# 4) у объекта можно “перекрыть” атрибут класса
class A:
    x = 1
p = A()
p.x = 7
print(A.x, p.x)


# 5) проверка/получение атрибута (hasattr/getattr)
class Person:
    age = 36
print(hasattr(Person, "age"))
print(getattr(Person, "age"))
