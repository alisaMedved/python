# исключение можно обрабатывать на любом уровне распространения исключения/стека вызова

def f1():
    return 1/0
def f2():
    return f1()
f2()

# ZeroDivisionError: division by zero

