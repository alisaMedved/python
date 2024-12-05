
# Словари

dictionary = {
    'a': 'A',
    'b': 'B',
    100: ['tr', 45, {'bg': 56}],
    'erw': {'bird': 'duck', 'animal': 'cat'},
    3: 2908,
    'field_for_delete': 654
}

# Знакомые нам методы из JS - выдают ключи, значения, пары ключ-значение
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# как всегда проверку существования - лучше делать через in или not in
print(3 not in dictionary)

# Момент с выдачей значения словаря
# Попытка достать значение несуществующего ключа через синтаксис dict[key] выдаст ошибку
# print(dictionary['not_existed_key'])
# Попытка достать значение несуществующего ключа через синтаксис dict.get(key, defaultValue) не выдаст ошибку
# defaultValue - необязательный аргумент, и если его нет то выдается None
print(dictionary.get('not_existed_key', [45, 'len']))

# удаление поля
del dictionary['field_for_delete']

# перезапись и запись новых полей
dictionary[44] = 'Jack'
dictionary[100] = dictionary[100] + ['meow']
print(dictionary)

# Автоматический перевод в список через list() выдает список ключей в порядке их добавления
# sorted(dict) - тоже выдает список ключей, но в отсортированном порядке в порядке увеличения
print(list(dictionary))
ger = {'b': 'gdr', 'w': 'wwfgty', 'a': 'ert4', 'W': 'wertgvu6'}
# ['W', 'a', 'b', 'w'] - сначала заглавные буквы, потом прописные
print(sorted(ger))

# Конструктор dict принимает в себя последовательность пар ключ-значение
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# вот такой синтаксис применим только если все ключи являются строками
print(dict(sape=4139, guido=4127, jack=4098))

"""Какие типы могут быть ключами у словаря? Неизменяемые. 
А именно: все примитивы (строки, все типы чисел, boolean) а также кортеж и frozenset
"""

dictAllKeys = {
    'bla': 6567,
    5: 'rew',
    (5, 7, 9): 'reee',
    True: 65,
    False: 200,
}

print(dictAllKeys[True])
print(dictAllKeys[(5, 7, 9)])

# немного о способах создания

# генератор словаря
dictFromGen = {x: x**2 for x in (2, 4, 6)}
print(dictFromGen)

"""
В конструктор dict можно вставить итерируемый объект.
Каждый элемент в итерируемом объекте сам по себе должен быть итерируемым объектом ровно с двумя элементами. 
Первый элемент каждого элемента становится ключом в новом словаре, 
а второй элемент — соответствующим значением. 
Если ключ встречается более одного раза, последнее значение для этого ключа становится соответствующим значением в новом словаре.
"""
dict_from_zip = dict(zip([1, 2, 3], ['a', 'b', 'c']))
print('dict_from_zip', dict_from_zip)

# итерация по items
for name, value in dict_from_zip.items():
    print(name, value)

iterator_view_object = iter(dict_from_zip.items())

# итератор по view object у items
for name, value in dict_from_zip.items():
    print(iterator_view_object.__next__())

dict_from_iter = dict(iter(dict_from_zip.items()))
print('dict_from_iter', dict_from_iter)
