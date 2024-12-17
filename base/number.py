number = 123345566

res1 = 15/10
# целочисленное деление
res2 = 15//10
res3 = 15%10
res4 = 5*3
# возведение в степень
res5 = 5**3

print(res1)
print(res2)
print(res3)
print(res4)
print(res5)

import math

print(math.fabs(-45))
print(abs(-45))
print(math.ceil(5.1))
# print пробелы сам ставит
print('math.floor(5.9)', math.floor(5.9))
print(round(5.8))

# всегда округление вниз
print('int(5.9)', int(5.9))

# random
# Все методы этого модуля являются методами скрытого экземпляра класса random.Random
# и ты можешь создать свой экземпляр (ну вдруг тебе понадобится новый нерасшариваемый state)

import random

# Почти Все методы этого модуля зависят от random.random() - случайное число от 0 до 1
# не подходит для криптографических целей
print(random.random())
print(random.randint(0, 10))

# - возвращает случайно выбранное число из range.
print(random.randrange(-10, 10, 2))

list1 = ['mas', '677', 'fgfht', 'ty', 'uih', 'ttyhb46', 'shark', 'monkey', 'camel', 'bear', 'fox', 'snake']
# - случайный элемент непустой последовательности.
print(random.choice(list1))
# - список длиной k из последовательности.
print(random.sample(list1, 5))
print(random.sample(range(300, 10000000, 6), 60))

for i in range(5):

    # Any number can be used in place of '11'.
    random.seed(11)

    # Generated random number will be between 1 to 1000.
    print(random.randint(1, 1000))





