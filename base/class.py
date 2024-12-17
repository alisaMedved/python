class Book:
    "It is class for book frm library"
    # атрибуты класса
    title = "Заголовок"
    pages = 143
    color: "red"

    # метод класса
    def set_title(self, title):
        pass

    def set_animals(self, animals):
        self.animals = animals

    def get_animals(self):
        return self.animals

def filter_by_double(dict_of_arg):
    filtered_items = []
    for (key, value) in dict_of_arg.items():
        if key == '__annotations__' or key == '__doc__' or key == '__dict__' or key.find('__') == -1:
            filtered_items.append((key, value))
            print(f"{key} : {value}")
    print("")
    return filtered_items

# словарь атрибутов класса и их значений
print(filter_by_double(Book.__dict__))

# экземпляры класса, объекты класса
book_1 = Book()
book_2 = Book()

# переопределение и создание свойств класса
Book.title = "Meow"
Book.title1 = "Meow1"
print(filter_by_double(Book.__dict__))

# При создании локального свойства и именно оно будет отображаться в экземпляре, а не одноименное из класса.
# Принцип того что при наследовании, значение поля находят в ближайшем из цепочки прототипов, а если не находят - тогда None
book_1.color = "black"
print('book_1.__dict__', filter_by_double(book_1.__dict__), 'Book.__dict__', filter_by_double(Book.__dict__))
print('book_2.__dict__', filter_by_double(book_2.__dict__), 'Book.__dict__', filter_by_double(Book.__dict__))
# выдает ошибку
# print(r"book_1.get('gfj')", book_1.gfj)
# print(r"Book.get('gfj')", Book.gfj)

# локальные атрибуты (свойства) объекта класса - это те, которые принадлежат только экземпляру
book_1.year = 2022
book_1.name = "name"
# словарь локальных атрибутов класса и их значений
print(filter_by_double(book_1.__dict__))

# Каким термином из ООП можно охарактеризовать универсальность интерфейса доступа к разным типам данных?
# Полиморфизм

print(type(book_1))
print(type(book_1) == Book)
print(isinstance(book_1, Book))

# способ создавать и изменять свойства в определенном пространстве имен

setattr(Book, "job", ["coder", "tester", "analytic"])
setattr(Book, "pages", 800)

setattr(book_1, "seasons", ["winter", "summer", "spring"])
setattr(book_1, "author", "John Carol")

print(book_1.__dict__)
print(Book.__dict__)

# Способ вытаскивать значения из пространства имен без ошибок
print(getattr(book_1, 'gfj', None))
print(getattr(Book, 'gfj', None))
print(getattr(Book, 'job'))
print(getattr(book_1, 'seasons'))

# Удаление свойств из классов и объектов
delattr(Book, 'job')
delattr(book_1, 'seasons')

del book_1.year
del Book.title

# выдает ошибку
# delattr(book_1, 'gfj')
# delattr(Book, 'gfj')

print(book_1.__dict__)
print(Book.__dict__)

# Проверка есть ли поля
print(hasattr(book_1, 'gfj'))
print(hasattr(Book, 'gfj'))

print(hasattr(book_1, 'author'))
print(hasattr(Book, 'pages'))

# Описание класса
print(Book.__doc__)

"""
Класс описывает шаблон для формирования его объектов.

Класс образует пространство имен для переменных и методов, объявленных в нем.

Каждый класс (объявленный в программе) можно воспринимать как новый (пользовательский) тип данных.
"""

book_3 = Book()
book_3.set_animals(['cat', 'dog'])
print(book_3.get_animals())

# методы - это тоже атрибуты класса
fn_set_animals = book_3.set_animals
fn_get_animals = book_3.get_animals

fn_set_animals(['camel', 'tiger'])
print(fn_get_animals())

"""
При instance_object = CustomClass() вызывается метод __call__(self)



Сначала создается экземпляр класса с помощью магического метода __new__

Потом инициализируется экземпляр класса с помощью магического метода __init__(self)

Удаляется экземпляр с помощью __del__(self) (ясен пень что мы можем в нем похимичить и отложить удаление)

Потом когда не останется ни одной внешней ссылки на класс - сборщик мусора Gorbage Collection 
и удалит класс

"""

class Point:
    figure = 'line'
    # конструктор - инициализатор класса
    def __init__(self, x=10, y=10):
        print('meow init')
        self.x = x
        self.y = y

    # финализатор класса
    def __del__(self):
        print('meow del', str(self))


point = Point(5)

# Реализуем паттерн Singleton: мы создали класс и за время его существрвания должен существовать только один экземпляр

class DataBase:
    # ссылка на последний из созданных экземпляр класса
    __instance = None
    pod = '134.788.009'
    type_data_base = 'sql'

    # вызывается при instance_object = CustomClass()
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj, *args, **kwargs)
        return obj

    # вызывается перед созданием экземпляра класса
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, root, user, port):
        self.root = root
        self.user = user
        self.port = port

    def get_data(self):
        return (self.root, self.user, self.port)

user_1 = DataBase('root', 'Nina', 80)
user_2 = DataBase('root', 'Lena', 40)

print(id(user_1), id(user_2))
print(user_1 is user_2)
print(user_1 is user_2)
print(user_1.get_data())
print(user_2.get_data())

class Line:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x1, y1):
        self.x1 = 0
        self.y1 = 0
        if self.validate(x1) and self.validate(y1):
            self.x1 = x1
            self.y1 = y1

    def get_coords(self):
        if not (self.validate(self.x1) and self.validate(self.y1)):
            return self.x1, self.y1
        return self.get_summ_of_quares(self.x1, self.y1)

    # вызывается когда от имени экземпляра спрашивают несуществующее свойство
    def __getattr__(self, item):
        raise AttributeError('Такого атрибута нет')

    # вызывается когда от имени экземпляра спрашивают существующее свойство
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    # вызывается при создании и изменении свойства экземпляра
    def __setattr__(self, item, value):
        object.__setattr__(self, item, value)

    # вызывается при удалении свойства экземпляра
    def __delattr__(self, item):
        object.__delattr__(self, item)

    @staticmethod
    def get_summ_of_quares(x, y):
        return x ** 2 + y ** 2

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD


line_1 = Line(5, 50)
print(line_1.get_coords())

"""
protected
def __validate() 
self.__x = x
__MIN_COORD = 10

private
def _validate() 
self._x = x
_MIN_COORD = 10

public
def validate() 
self.x = x
MIN_COORD = 10

Но можно обойти
point = Point(10, 20)
point._Point__validate(50)

Но так неправильно и лучше писать геттеры и сеттеры - ведь есть негласное правило обращаться извне класса от имени экземпляра
только к публичным методам и свойствам

from accessify import private protected

@private
@classmethod
def validate(cls, arg):

@protected
@staticmethod
def get_sum_of_quares(x, y):
"""

# Создание функтора
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter

c = Counter()
c1 = Counter()
c()
c1(-5)
c(12)
c()
print(c(), c1())

# Замена замыкания функции - потом доправишь пример

# class StripChars:
#     def __call__(self, stripSymbol=' ', chars='abcdefghij'):
#         if not isinstance(chars, str):
#             raise TypeError("Аргумент должен быть строкой")
#         instance_str = self.__new__(args[0].strip(self.__chars, stripSymbol))
#         self.__init__(instance_str)
#         return instance_str
#
#     def __init__(self, chars):
#         self.__chars = chars
#
# s1 = StripChars(stripSymbol='!', 'abc')

# Создание декораторов

import math

class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x))/dx

@Derivate
def df_sin(x):
    return math.sin(x)

# Аналог df_sin = Derivate(df_sin)

print(df_sin(math.pi/3))


class Cat:
    def __init__(self, name):
        self.name = name
    # для отображения информации об экземпляре класса для разраба - в Python console введи cat
    def __repr__(self):
        return f"{self.__class__}: {self.name} yyuuj"

    # для отображения информации об экземпляре класса для пользователя print(cat)
    def __str__(self):
        return f"{self.name} 5667"

cat = Cat("Vasya")
print('hjj', cat)


class CoordsPoint:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

coords_point = CoordsPoint(1, 2, 3)
print(len(coords_point))
print(abs(coords_point))

# Методы арифмитических операций
"""
__add__() - сложение
__sub__() - вычитание
__mul__() - умножение
__truediv__() - деление
"""

# Методы сравнений
"""
__eq__() - ==
__ne__() - !=
__lt__() - <
__le__() - <=
__gt__() - >
__ge__() - >=
"""

"""
Для каждого объекта Python создает hash
у одинаковых объектов hash будет равен

Редко но бывает:
1) у одинаковых объектов всегда одинаковый hash
2) но одинаковые hash не означают одинаковые объекты

hash можно рассчитать только для неизменяемых объектов
"""

print(hash(123))
ac = 123
print(hash(ac))
bf=123
print(hash(bf))
print(hash(740))


print(hash((123, 450)))
ac = (123, 450)
print(hash(ac))
bf=(123, 450)
print(hash(bf))
print(hash((740, 54)))

"""
На самом деле под капотом у Python у dict

key = (hash(key), key) - для более быстрого поиска значений полей dict поиск идет по hash
__hash__(self)
"""

"""
При превращении типа в bool вызывается метод __bool__(self), а если его нет
то __len__(self)
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__counter = 0
        self.marks = list(marks)

    # вызывается когда student[2]
    def __getitem__(self, item):
        return self.marks[item]

    # вызывается когда student[2] = 4
    def __setitem__(self, key, value):
        self.marks[key] = value

    # del student[2]
    def __delitem__(self, key):
        del self.marks[key]

    # def __iter__(self):
    #     return iter(self.marks)

    def __next__(self):
        self.__counter += 1
        if self.__counter == len(self.marks) - 3:
            raise StopIteration
        else:
            return 'meow', self.marks[self.__counter]


student = Student('John', [5, 4, 5, 3, 2, 5])
print(student[2])
student[2] = 3
print(student[2])
del student[2]
print(student.marks)

for i in student:
    print(i)

student_1 = Student('John', [5, 4, 5, 5, 2, 5])
for i in student_1:
    print(i)

# наследование - extends

class Geom:
    name = 'rtyt'

class Lineee(Geom):
    def draw_figure(self):
        print('draw')

l = Lineee()
print(l.draw_figure())
print(l.name)

from dataclasses import dataclass

@dataclass
class Entity:
    health: int

@dataclass
class Human(Entity):
    pass

a = Human(1)
print(a.health == 1)