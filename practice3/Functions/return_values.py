# 1) вернуть число
def f():
    return 5
print(f())


# 2) вернуть строку
def hello(name):
    return "Hello " + name
print(hello("Emil"))


# 3) вернуть список
def fruits():
    return ["apple", "banana", "cherry"]
print(fruits()[0])


# 4) вернуть результат вычисления
def area_square(a):
    return a * a
print(area_square(7))


# 5) ранний return
def sign(x):
    if x >= 0:
        return "non-negative"
    return "negative"
print(sign(-3))
