str1 = """Я могу не экранировать ': " ничего в том числе кавычки"""
str2 = '''Я могу не экранировать ': " ничего в том числе кавычки'''

# Попробуем многострочные

strMulty = """Я могу 
не экранировать ':
 " нич
 его"""

# сырые строки в print
print(str1)
print(str2)
print(strMulty)

print(r'new\nstring')
print('new\nstring')

# не ставит автоматом пробелы
strRes = str1 + str2
print(strRes)
print(str1 + str2)
# а через запятую print ставит автоматом пробелы
print(str1, str2)
# умножение строк
print('ghh' * 5)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# по индексу - a
print('первый элемент', alphabet[0])
# первый элемент с конца - z
print('первый элемент с конца', alphabet[-1])
# slice с дефолтными значениями
print('slice с дефолтными значениями', alphabet[0:len(alphabet):1])
# slice вся строка только символы перечисляются с шагом 2 - 'acegikmoqsuwy'
print('slice вся строка только символы перечисляются с шагом 2', alphabet[::2])
# slice вся строка только символы перечисляются с конца строки - аналог reversed, только reversed возвращает обратный итератор
print('slice reversed', alphabet[::-1])
print('slice reversed с шагом 2', alphabet[::-2])
# Но так откровенно говоря писать костыльно и гадко
print('slice reversed с помощью функции reversed', ''.join(reversed(alphabet)))
# slice вся строка до 8-го индекса - 'abcdefgh'
print('slice вся строка до 8-го индекса', alphabet[0:8:1])
# slice вся строка до 8-го индекса только символы перечисляются с шагом 2 - 'aceg'
print('slice вся строка до 8-го индекса только символы перечисляются с шагом 2', alphabet[0:8:2])
# lowerCase и upperCase
print(alphabet.upper())
print(alphabet.lower())
print(alphabet.capitalize())


s = "Hello World! Hello Python!"

# Replace "Hello" with "Hi"
s1 = s.replace("Hello", "Hi")
# сколько раз входит подстрока чувствительный к регистру
print(s.count('h'))
print(s.count('H'))
# находится ли вообще подстрока
print('Py' in 'Python')

print(s1)

# Как вставлять в строку рассчитываемые значения?
# Лучше всего через f-strings
name = 'Fred'
age = 42
filledTemplate = f'He said his name is {name + ' Tinger'} and he is {age - 23} years old.'
print(filledTemplate)

Student = [('Ram', 90), ('Ankit', 78), ('Bob', 92)]
for i in Student:
    studentTemplate = f'He said his name is {i[0] + ' Tinger'} and he is {i[1] - 45} years old.'
    print(studentTemplate)

# как trim делать?

greeting = "     Hello!  "

print(greeting.strip(), "How are you?")
# только справа убрать пробелы
print(greeting.rstrip(), "How are you?")
# только слева убрать пробелы
print(greeting.lstrip(), "How are you?")

enthusiastic_greeting = "!!! Hello !!!!"

print(enthusiastic_greeting.strip('!'), "How are you?")
# только справа убрать определенные символы
print(enthusiastic_greeting.rstrip('!'), "How are you?")
# только слева убрать определенные символы
print(enthusiastic_greeting.lstrip('!'), "How are you?")

# Как вставлять в строку рассчитываемые значения?
# Старые способы

print('{third} dfghjkl {1} ghjk {0}'.format(name, age, third='Rebeka'))
# вот у этого способа много модификаторов всяких
print('%s dfghjkl %s ghjk %s' % (name, age, 'Rebeka'))

