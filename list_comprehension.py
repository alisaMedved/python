from itertools import zip_longest

squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)

squares_cubes = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
# [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]
print(squares_cubes)

first = [x for x in range(1, 5, 1)]
second = [y for y in range(5, 1, -1)]
pairs = [(x if x!=y else 'alcohol', y if x!=y else 'drags') for x in range(1, 5, 1) for y in range(5, 1, -1)]
print('first', first)
print('second', second)
print('pairs', pairs)

# а вот встроенная функция zip выдает список кортежей в параллельной итерации
another_pairs = list(zip([1, 2, 3], ['a', 'b', 'c']))
# выдаст ошибку в строгом режиме - если списки не одинаковой длины
# another_pairs = list(zip([1, 2, 3], ['a', 'b'], strict=True))
print('another_pairs', another_pairs)

import itertools
pairs_with_default = list(itertools.zip_longest([1, 2, 3], ['a', 'b'], fillvalue='meow'))
print('pairs_with_default', pairs_with_default)

vec = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
flatten = [digit for lst in vec for elem in lst for digit in elem]
print(flatten)

animals = {key: value for key, value in zip([1, 2, 3], ['a', 'b', 'c'])}
print('animals', animals)
dict_from_zip = dict(zip([1, 2, 3], ['a', 'b', 'c']))
print('dict_from_zip', dict_from_zip)

# Рассмотрим еще итерации по вложенным спискам и как транспонировать матрицу

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

# Транспонируй матрицу

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
transposed_zip = [list(column) for column in zip(*matrix)]
print('columns', transposed)
print('columns transposed_zip', transposed_zip)