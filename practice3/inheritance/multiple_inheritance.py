# 1) класс наследуется от двух
class A:
    def a(self): print("A")
class B:
    def b(self): print("B")
class C(A, B):
    pass
C().a(); C().b()


# 2) конфликт имён: берётся по MRO (слева направо)
class A:
    def f(self): print("A")
class B:
    def f(self): print("B")
class C(A, B):
    pass
C().f()   # A


# 3) можно явно вызвать нужный метод
B.f(C())


# 4) миксин-стиль
class Logger:
    def log(self, msg): print("LOG:", msg)
class Service(Logger):
    def run(self): self.log("running")
Service().run()


# 5) super() в цепочке (упрощённо)
class A:
    def f(self): print("A")
class B(A):
    def f(self):
        super().f()
        print("B")
B().f()
