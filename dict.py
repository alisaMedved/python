
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
print(list(dictionary.keys()))
print(list(dictionary.values()))
print(list(dictionary.items()))

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

"""Дописать раздел - кто может быть ключами - потому что тут больше вариации чем в JS и все веселее"""

# генератор словаря
dictFromGen = {x: x**2 for x in (2, 4, 6)}
print(dictFromGen)