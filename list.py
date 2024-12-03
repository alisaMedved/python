
list2 = [6784, 'uih', [[0, 8], 'yui']]
# дефолтный slice start 0 : кол-во эл-тов : шаг 1
print('дефолтный slice start 0 : кол-во эл-тов : шаг 1', list2[::])
# обращение к эл-ту списка
print('обращение к эл-ту списка', list2[2][1])

# умножение списка
list1 = [56, 'hjy', '543333', 9.76]
print('умножение списка', list1 * 5)
# [56, 'hjy', '543333', 9.76, 56, 'hjy', '543333', 9.76, 56, 'hjy', '543333', 9.76, 56, 'hjy', '543333', 9.76, 56, 'hjy', '543333', 9.76]

# сложение списков - по сути concat списков без мутации
resList = list1 + list2
print('сложение списков - по сути concat списков без мутации:', resList)

# добавление одного эл-та к списку - мутирует исходный список
list1.append('finish')
print('добавление одного эл-та к списку - не мутирует исходный список', list1)
# concat списков - мутирует только первый исходный список, второй остается нетронутым
list1.extend(list2)
print('concat списков', list1)
print('concat списков', list2)

# Удалить эл-т списка
list3 = ['camel', 'banana', 'palm_tree', 'pineapple', 'monkey', 'racoon', 'cat', 'dog', 'sand', 'sun', 'sea', 'sky', 'fish']
print('pop - Удаляет и возвращает последний эл-т списка', len(list3), list3.pop(), len(list3))
print('pop - Удаляет и возвращает эл-т списка по индексу', len(list3), list3.pop(5), len(list3))
list3.remove('banana')
print('remove - Удаляет первый эл-т списка который равен значению', len(list3), list3)

# Вставка эл-та списка
# insert Первый аргумент — это индекс элемента, перед которым нужно вставить
list4_1 = [1, 2, 3, 4, 5, 6, 7, 'y']
list4_1.insert(0, 'banana')
print(list4_1)
list4_2 = [1, 2, 3, 4, 5, 6, 7, 'y']
list4_2.insert(len(list4_2), 'banana')
print(list4_2)
list4_2.pop()
list4_2.append('banana')
print(list4_2)

# Присваивание с каким-то непонятным синтаксисом - НАДО РАЗОБРАТЬ!!!
list5_1 = [1, 2, 3, 4, 5, 6, 7, 'y']
list5_1[len(list5_1):] = [78]
print(list5_1)

list5_2 = [1, 2, 3, 4, 5, 6, 7, 'y']
list5_2[len(list5_2):] = [788, 'hjk', 60]
print(list5_2)

# удалить все элементы списка
listForDel =[1, 2, 3, 4, 5, 6, 7, 'y']
listForDel.clear()
print(listForDel)

# непонятным синтаксисом - НАДО РАЗОБРАТЬ!!!
listForDel1 =[1, 2, 3, 4, 5, 6, 7, 'y']
del listForDel1[:]
print(listForDel1)

# reverse
listForReverse = [1, 2, 3, 4, 5, 6, 7, 'y']
listForReverse.reverse()
print(listForReverse)

listForReverse1 = [1, 2, 3, 4, 5, 6, 7, 'y']
# reversed - Возвращаемое значение: обратный итератор.
reversedIterator = reversed(listForReverse1)
print(list(reversedIterator))

# sort
# listForSort = ['camel', 'banana', 'palm_tree', 'pineapple', 'monkey', 'racoon', 'cat', 'dog', 'sand', 'sun', 'sea', 'sky', 'fish']
# listForSort.sort()

"""
Метод списка изменяет исходный список, функция же sorted не изменяет его а создает новый отсортированный список
"""

# index - верни индекс эл-та который равен значению
listForIndexOf = [1, 2, 3, 4, 5, 6, 7, 'y']
print(listForIndexOf.index('y'))

# index - верни индекс эл-та который равен значению
listForIndexOf = [1, 2, 3, 4, 5, 6, 7, 'y']
print(listForIndexOf.index('y'))

# Возвращает количество появлений x в списке.
listForSearchCount = [1, 'y', 3, 'y', 5, 6, 7, 'y']
print(listForSearchCount.count('y'))
print('y' in listForSearchCount)

# Неглубокая копия списка
initialList = [89, 'hjj', ['uii', 954, ['tyuy', [['dog', 'bark'], ['meow', 'cat']]], 'jii']]
copyOfList = initialList.copy()
print(copyOfList[2][2][1][0][0])




