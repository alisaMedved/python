
# False
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(0))
print(bool(None))

# if else elif
a = 10

if a > 5 or a < 0:
    print('Правда')
    if a % 2 == 0:
        print('this even number', a)
    else:
        print('this odd number', a)
elif a == 3:
    print('Правда 3')
else:
    print('Ложь 3')

#  assignment expression (sometimes also called a “named expression” or “walrus”)

def do_something(match) :
    print(match)

import re
pattern = re.compile("[a-zA-Z]+]")

# вот тут мы объявляем assignment expression с помощью :=
""" matching := pattern.search('FRdfhjklu hhjkk ftgyjk') """
# := означает вычисление, возврат значения и присвоение его переменной
# единственное когда это захочется использовать это в случае вычисляемой переменной в условиях,
# которую потом будешь использовать и не хочешь заново вычислять

if matching := pattern.search('FRdfhjklu hhjkk ftgyjk'):
    do_something(matching)

# while chunk := file.read(9000):
#     process(chunk)

while a < 20:
    a = a + 1
    print('while cycle', a)

# Тернарные операторы - как и в JS есть краткая запись if else и запись через or.
# Присмотрись у python динамическая типизация
is_nice = True
state = "nice" if is_nice else "not nice"

def calc_weight(animal):
   # return animal.get('weight_animal') if animal.get('weight_animal') else animal.get('weight')
    return animal.get('weight_animal') or animal.get('weight')

cat = {'weight_animal': 4000}
dog = {'weight': 8000}
print(calc_weight(cat))
print(calc_weight(dog))

# match case - аналог switch case из JS
# Важные замечания
# 1) в match case не может быть break - он может быть только в try/catch/finally, in while, in for
# 2) можно case делать без return, его можно юзать если match case в функции/методе
# шаблон как литерал
status = 400
match status:
    case 400:
        print('Bad Request')
    case 200:
        print('ok')
    case 401 | 403 | 404:
        print("Not allowed")
    case _:
        raise ValueError("Not a http_code")

# Шаблоны как capture

def greet(name = None):
    match name:
        case None:
            print('Hey there')
        case name_smb:
            print(f'Hello {name_smb}')
greet()
greet('Mario')

# Шаблон как подстановки (wildcard) - это использование _
# _ используют для default case и для перечисления аргументов, которые нам не нужны

cords = [100, 200]
def model_of_coords(cordinats):
    match cordinats:
        case [_]:
            print('1D model')
        case [_, _,]:
            print('2D Model')
        case [_, _, _,]:
            print('3D Model')

model_of_coords(cords)

# Шаблон постоянных значений и перечисления

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

def view_colors(color):
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")

view_colors(Color.RED)

# Шаблон последовательностей

another_cords = [100, 200]
def model_with_coords(cordinats):
    match cordinats:
        case x, :
            print(f'1D model {x}')
        case x, y:
            print(f'2D Model {x} {y}')
        case x, y, z:
            print(f'3D Model {x} {y} {z}')

model_with_coords(another_cords)



