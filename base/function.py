# recursion
import asyncio

vec = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

def flatten_list(nested_list):
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                flatten(item)
            else:
                flat_list.append(item)

    flat_list = []
    flatten(nested_list)
    return flat_list

print(flatten_list(vec))

# досрочный конец выполнения скрипта exit(0)
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])
    if a[i] == 'a':
        # exit(0)
        pass

# именованная передаче аргумента

def message_print(message, end):
    print(message, end=end)

message_print('Hello World!', ' Meow \n')
message_print(message='Hello World!', end=' Meow \n')

# функция, включающая и позиционные, и именованные аргументы
def add_numbers(num0, num1, num2=2, num3=3):
     outcome = num0 + num1 + num2 + num3
     print(f"num0={num0}, num1={num1}, num2={num2}, num3={num3}")
     return outcome
 
add_numbers(0, 1)
add_numbers(0, 1, num3=4, num2=5)
add_numbers(num0=0, num1=1, num2=5, num3=4)

# много позиционных аргументов функции *args --> КОРТЕЖ аргументов
from functools import reduce

def squares_reduce(*args):
    print(args)
    print(list(args))
    return reduce(squares, list(args), [])

def squares(acc, elm):
    acc.append(elm**2)
    return acc

print(squares_reduce(1, 2, 3, 8, 0))

# много именованных аргументов функции **kwargs --> СЛОВАРЬ аргументов

def func_dict(**kwargs):
    print(kwargs)
    print(kwargs['nure'])

print(func_dict(numq=1, ser=2, nure=3, gera='trr'))


# возврат двух и более значений из функции --> КОРТЕЖ значений

def upper_and_lower(string):
    return string.upper(), string.lower()

upper, lower = upper_and_lower('Hello World!')
print(upper)
print(lower)

# лямбда функции

#  Лямбда и условные операторы

max_number = lambda a, b: a if a > b else b
print(max_number(3, 5))

# Лямбда вызывает лямбду

current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(result)

# Эта функция может иметь любое количество аргументов, но вычисляет и возвращает только одно значение
#
# Лямбда-функции применимы везде, где требуются объекты-функции
#
# Вы должны помнить, что синтаксически лямбда-функция ограничена, позволяет представить всего одно выражение
#
# Они имеют множество вариантов применения в конкретных областях программирования, наряду с другими типами выражений, используемых в функциях.

"""
Без использования лямбды: Здесь обе функции возвращают заданное значение, возведенное в куб. 
Но при использовании def, нам пришлось определить функцию с именем и defined_cube() дать ей входную величину.  
После выполнения нам также понадобилось возвратить результат, из того места, откуда была вызвана функция,
 и мы сделали это, используя ключевое слово return.

С применением лямбды: Определение лямбды не включает оператор return, а всегда содержит возвращенное выражение. 
Мы также можем поместить определение лямбды в любое место, где ожидается функция, и нам не нужно присваивать его переменной. 
Так выглядят простые лямбда-функции.
"""

async def ree():
    await asyncio.sleep(1)
