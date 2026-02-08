# 1) простая функция
def hello():
    print("Hello")
hello()


# 2) функция с параметром
def greet(name):
    print("Hello", name)
greet("Emil")


# 3) функция вызывается несколько раз
def shout():
    print("Hey!")
shout(); shout()


# 4) функция внутри использует переменные
def add_one(x):
    print(x + 1)
add_one(10)


# 5) пустое тело (заглушка)
def todo():
    pass
