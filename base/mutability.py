# Списки, словари и множества - изменяемые!!!

""" Спасибо Python, теперь нам приходится писать эти примеры в JS """

# Пример 1 - изменяем переменную, которой присвоили ссылку на переменную
mas = [1, 3, 7]
mas1 = mas
print('mas ', mas)
print('mas1 ', mas1)

mas1[0] = 88

print('mas ', mas)
print('mas1 ', mas1)

# Пример 2 - изменяем список исходный
mas2 = [1, 3, 7]
mas3 = mas2

print('mas2 ', mas2)
print('mas3 ', mas3)

mas2[0] = 88

print('mas2 ', mas2)
print('mas3 ', mas3)

"""
 * Ссылочные типы данных ссылаются не на значения, а на ссылки.
 *  И потому при изменении одной переменной, меняются обе переменные: и та что исходного списка
 *  и та которой присвоили ссылку на исходный массив.
 *
 *  Потому что на самом деле - они обе содержат ссылку на массив, и ни одна из них не содержит сам массив
"""

""" Способы это обойти - создать копию, а не просто ссылку """

# Пример 1 - изменяем переменную, которой присвоили ссылку на переменную
masForDeep = [1, 3, 7]
masForDeep1 = masForDeep.copy()
print('masForDeep ', masForDeep)
print('masForDeep1 ', masForDeep1)

masForDeep1[0] = 88

print('masForDeep ', masForDeep)
print('masForDeep1 ', masForDeep1)

# Пример 2 - изменяем список исходный
masForDeep2 = [1, 3, 7]
masForDeep3 = masForDeep2.copy()

print('masForDeep2 ', masForDeep2)
print('masForDeep3 ', masForDeep3)

masForDeep2[0] = 88

print('masForDeep2 ', masForDeep2)
print('masForDeep3 ', masForDeep3)

""" Еще способ это обойти - это сделать новую инициализацию нового списка - например с помощью конструктора list() """
# Конструктор list() преобразует итерируемый объект (словарь, кортеж, строку и т. д.) в список и возвращает его.

# Пример 1 - изменяем переменную, которой присвоили ссылку на переменную
masNewInit = [1, 3, 7]
masNewInit1 = list(masNewInit)
print('masNewInit ', masNewInit)
print('masNewInit1 ', masNewInit1)

masNewInit1[0] = 88

print('masNewInit ', masNewInit)
print('masNewInit1 ', masNewInit1)

# Пример 2 - изменяем список исходный
masNewInit2 = [1, 3, 7]
masNewInit3 = list(masNewInit2)

print('masNewInit2 ', masNewInit2)
print('masNewInit3 ', masNewInit3)

masNewInit2[0] = 88

print('masNewInit2 ', masNewInit2)
print('masNewInit3 ', masNewInit3)

""" Создаем по сути глубокую копию через JSON - но тут на самом деле срабатывает то как раз механизм инициализации """

import json

# Пример 1 - изменяем переменную, которой присвоили ссылку на переменную
masJson = [1, 3, 7]
masJson1 = json.loads(json.dumps(masJson))
print('masJson ', masJson)
print('masJson1 ', masJson1)

masJson1[0] = 88

print('masJson ', masJson)
print('masJson1 ', masJson1)

# Пример 2 - изменяем список исходный
masJson2 = [1, 3, 7]
masJson3 = json.loads(json.dumps(masJson2))

print('masJson2 ', masJson2)
print('masJson3 ', masJson3)

masJson2[0] = 88

print('masJson2 ', masJson2)
print('masJson3 ', masJson3)

""" Случай с вложенными структурами данных, и когда мы не делаем deep copy на всех уровнях вложенности. """

# В этот раз будем использовать аналог метода списка copy - метод неглубокого копирования copy из модуля copy

import copy

# Пример 1 - изменяем переменную, которой присвоили ссылку на переменную
masSemiDeep = [[56, 900], 3, 7,]
masSemiDeep1 = copy.copy(masSemiDeep)
print('masSemiDeep ', masSemiDeep)
print('masSemiDeep1 ', masSemiDeep1)

masSemiDeep1[0][0] = 88

print('masSemiDeep ', masSemiDeep)
print('masSemiDeep1 ', masSemiDeep1)

# Пример 2 - изменяем список исходный
masSemiDeep2 = [[56, 900], 3, 7,]
masSemiDeep3 = copy.copy(masSemiDeep2)

print('masSemiDeep2 ', masSemiDeep2)
print('masSemiDeep3 ', masSemiDeep3)

masSemiDeep2[0][0] = 88

print('masSemiDeep2 ', masSemiDeep2)
print('masSemiDeep3 ', masSemiDeep3)

""" Случай с вложенными структурами данных, мы исправим это с помощью глубокой копии """

# Пример 1 - изменяем переменную, которой присвоили ссылку на переменную
masFullDeep = [[56, 900], 3, 7,]
masFullDeep1 = copy.deepcopy(masFullDeep)
print('masFullDeep ', masFullDeep)
print('masFullDeep1 ', masFullDeep1)

masFullDeep1[0][0] = 88

print('masFullDeep ', masFullDeep)
print('masFullDeep1 ', masFullDeep1)

# Пример 2 - изменяем список исходный
masFullDeep2 = [[56, 900], 3, 7,]
masFullDeep3 = copy.deepcopy(masFullDeep2)

print('masFullDeep2 ', masFullDeep2)
print('masFullDeep3 ', masFullDeep3)

masFullDeep2[0][0] = 88

print('masFullDeep2 ', masFullDeep2)
print('masFullDeep3 ', masFullDeep3)

"""
Изменяемые типы данных: словари, списки, множества
Неизменяемые типы данных: примитивы, и frozenset и кортежи
"""

tuple1 = (5, 8, 90)
tuple2 = tuple1

print('tuple1 ', tuple1)
print('tuple2 ', tuple2)
