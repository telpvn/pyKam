# Подробный справочник по типам данных Python

## Содержание
1. [Основные встроенные типы данных](#основные-встроенные-типы-данных)
2. [Коллекции (подробно)](#коллекции-подробно)
3. [Специальные типы](#специальные-типы)
4. [Работа с типами](#работа-с-типами)

---

## Основные встроенные типы данных

### Числовые типы

#### int (Целые числа)
```python
# Создание
x = 42
y = int("123")
z = int(3.14)  # Усечение до 3

# Особенности
big_num = 123456789012345678901234567890  # Неограниченная точность
binary = 0b1010  # Двоичная система (10)
octal = 0o12     # Восьмеричная система (10)
hex_num = 0xFF   # Шестнадцатеричная система (255)

# Методы
num = 42
print(num.bit_length())  # Количество битов
print(num.to_bytes(4, 'big'))  # Преобразование в байты
```

#### float (Числа с плавающей точкой)
```python
# Создание
f1 = 3.14
f2 = 1.23e-4  # Научная нотация
f3 = float("inf")  # Бесконечность
f4 = float("nan")  # Not a Number

# Методы и свойства
import math
print(f1.is_integer())  # Проверка на целое
print(f1.hex())         # Шестнадцатеричное представление
print(math.isnan(f4))   # Проверка на NaN
print(math.isinf(f3))   # Проверка на бесконечность
```

#### complex (Комплексные числа)
```python
# Создание
c1 = 3 + 4j
c2 = complex(3, 4)
c3 = complex("3+4j")

# Свойства и методы
print(c1.real)      # Действительная часть: 3.0
print(c1.imag)      # Мнимая часть: 4.0
print(c1.conjugate())  # Сопряженное число: (3-4j)
print(abs(c1))      # Модуль: 5.0
```

### Логический тип

#### bool (Булевы значения)
```python
# Создание
b1 = True
b2 = False
b3 = bool(1)    # True
b4 = bool(0)    # False
b5 = bool([])   # False (пустая коллекция)
b6 = bool([1])  # True (непустая коллекция)

# Ложные значения в Python
falsy_values = [False, None, 0, 0.0, 0j, '', [], {}, set()]
```

### Текстовый тип

#### str (Строки)
```python
# Создание
s1 = "Hello"
s2 = 'World'
s3 = """Многострочная
строка"""
s4 = str(123)

# Методы
text = "Hello, World!"
print(text.upper())           # HELLO, WORLD!
print(text.lower())           # hello, world!
print(text.capitalize())      # Hello, world!
print(text.title())           # Hello, World!
print(text.swapcase())        # hELLO, wORLD!

# Поиск и проверка
print(text.find("World"))     # 7
print(text.index("World"))    # 7 (ValueError если не найдено)
print(text.count("l"))        # 3
print(text.startswith("Hello"))  # True
print(text.endswith("!"))     # True
print("123".isdigit())        # True
print("abc".isalpha())        # True
print("abc123".isalnum())     # True

# Разделение и объединение
words = text.split(", ")      # ['Hello', 'World!']
joined = "-".join(words)      # Hello-World!

# Замена
new_text = text.replace("World", "Python")  # Hello, Python!

# Форматирование
name = "Alice"
age = 25
formatted = f"Name: {name}, Age: {age}"  # f-строки
formatted2 = "Name: {}, Age: {}".format(name, age)
formatted3 = "Name: %(name)s, Age: %(age)d" % {"name": name, "age": age}
```

---

## Коллекции (подробно)

### list (Списки)

#### Основы работы со списками
```python
# Создание
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, [1, 2]]
from_range = list(range(5))  # [0, 1, 2, 3, 4]
comprehension = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Индексирование и срезы
lst = [0, 1, 2, 3, 4, 5]
print(lst[0])       # 0 (первый элемент)
print(lst[-1])      # 5 (последний элемент)
print(lst[1:4])     # [1, 2, 3] (срез)
print(lst[:3])      # [0, 1, 2] (начало до индекса 3)
print(lst[3:])      # [3, 4, 5] (с индекса 3 до конца)
print(lst[::2])     # [0, 2, 4] (каждый второй)
print(lst[::-1])    # [5, 4, 3, 2, 1, 0] (обратный порядок)
```

#### Методы списков
```python
# Добавление элементов
lst = [1, 2, 3]
lst.append(4)           # [1, 2, 3, 4] - добавить в конец
lst.insert(1, 'new')    # [1, 'new', 2, 3, 4] - вставить по индексу
lst.extend([5, 6])      # [1, 'new', 2, 3, 4, 5, 6] - добавить список

# Удаление элементов
lst.remove('new')       # Удалить первое вхождение
popped = lst.pop()      # Удалить и вернуть последний элемент
popped_index = lst.pop(0)  # Удалить и вернуть элемент по индексу
del lst[1]              # Удалить элемент по индексу
lst.clear()             # Очистить список

# Поиск и подсчет
lst = [1, 2, 3, 2, 4, 2]
print(lst.index(2))     # 1 (индекс первого вхождения)
print(lst.count(2))     # 3 (количество вхождений)
print(2 in lst)         # True (проверка наличия)

# Сортировка и изменение порядка
lst = [3, 1, 4, 1, 5]
lst.sort()              # [1, 1, 3, 4, 5] - сортировка на месте
lst.sort(reverse=True)  # [5, 4, 3, 1, 1] - обратная сортировка
lst.reverse()           # [1, 1, 3, 4, 5] - обратить порядок

# Копирование
original = [1, 2, [3, 4]]
shallow_copy = original.copy()  # или original[:]
import copy
deep_copy = copy.deepcopy(original)
```

#### Списковые включения (List Comprehensions)
```python
# Базовый синтаксис: [выражение for элемент in итерируемый_объект if условие]

# Простые примеры
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Работа со строками
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]  # ['HELLO', 'WORLD', 'PYTHON']
lengths = [len(word) for word in words]  # [5, 5, 6]

# Вложенные списки
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Условные выражения
numbers = [1, 2, 3, 4, 5]
modified = [x if x % 2 == 0 else -x for x in numbers]  # [-1, 2, -3, 4, -5]

# Множественные условия
filtered = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]  # [0, 6, 12, 18, ...]
```

### tuple (Кортежи)

#### Основы работы с кортежами
```python
# Создание
empty_tuple = ()
single_tuple = (1,)  # Запятая обязательна для одного элемента
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14)
from_list = tuple([1, 2, 3])
without_parentheses = 1, 2, 3  # Также создает кортеж

# Неизменяемость
# numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Индексирование (как у списков)
print(numbers[0])    # 1
print(numbers[-1])   # 5
print(numbers[1:4])  # (2, 3, 4)
```

#### Методы кортежей
```python
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))    # 3 - количество вхождений
print(t.index(3))    # 2 - индекс первого вхождения

# Распаковка кортежей
point = (3, 4)
x, y = point  # x = 3, y = 4

# Множественная распаковка
data = (1, 2, 3, 4, 5)
first, *middle, last = data  # first=1, middle=[2, 3, 4], last=5

# Обмен значений
a, b = 1, 2
a, b = b, a  # Теперь a=2, b=1
```

#### Именованные кортежи
```python
from collections import namedtuple

# Создание класса именованного кортежа
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')

# Использование
p = Point(3, 4)
print(p.x, p.y)  # 3 4
print(p[0], p[1])  # 3 4 (тоже работает)

person = Person('Alice', 25, 'Moscow')
print(person.name)  # Alice

# Методы именованных кортежей
print(person._asdict())  # OrderedDict([('name', 'Alice'), ('age', 25), ('city', 'Moscow')])
new_person = person._replace(age=26)  # Создать новый с измененным полем
print(Person._fields)  # ('name', 'age', 'city')
```

### dict (Словари)

#### Основы работы со словарями
```python
# Создание
empty_dict = {}
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
from_pairs = dict([('a', 1), ('b', 2)])
from_kwargs = dict(x=1, y=2, z=3)
comprehension = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Доступ к элементам
print(scores['Alice'])      # 95
print(scores.get('David'))  # None (безопасный доступ)
print(scores.get('David', 0))  # 0 (значение по умолчанию)

# Изменение и добавление
scores['David'] = 88        # Добавить новый элемент
scores['Alice'] = 98        # Изменить существующий
scores.update({'Eve': 91, 'Frank': 85})  # Добавить несколько
scores.update(George=89)    # Также можно так
```

#### Методы словарей
```python
data = {'a': 1, 'b': 2, 'c': 3}

# Получение ключей, значений, пар
print(list(data.keys()))    # ['a', 'b', 'c']
print(list(data.values()))  # [1, 2, 3]
print(list(data.items()))   # [('a', 1), ('b', 2), ('c', 3)]

# Удаление элементов
value = data.pop('b')       # Удалить и вернуть значение (2)
key, value = data.popitem() # Удалить и вернуть произвольную пару
del data['a']               # Удалить по ключу
data.clear()                # Очистить словарь

# Копирование
original = {'a': 1, 'b': [2, 3]}
shallow_copy = original.copy()
import copy
deep_copy = copy.deepcopy(original)

# Объединение словарей (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2      # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1 |= dict2              # Обновить dict1

# setdefault - установить значение, если ключа нет
data = {}
data.setdefault('items', []).append('new_item')  # Создать список, если его нет
```

#### Словарные включения
```python
# Базовый синтаксис: {ключ: значение for элемент in итерируемый if условие}

# Простые примеры
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Инвертирование словаря
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}  # {1: 'a', 2: 'b', 3: 'c'}

# Фильтрация словаря
data = {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 2}
expensive = {k: v for k, v in data.items() if v > 4}  # {'apple': 5, 'cherry': 8}
```

### set (Множества)

#### Основы работы с множествами
```python
# Создание
empty_set = set()  # {} создает пустой словарь!
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4} - дубликаты удаляются
from_string = set('hello')  # {'h', 'e', 'l', 'o'}
comprehension = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# Особенности множеств
# - Элементы уникальны
# - Неупорядоченные
# - Элементы должны быть хешируемыми (неизменяемыми)
```

#### Операции с множествами
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Объединение (союз)
union1 = set1 | set2        # {1, 2, 3, 4, 5, 6}
union2 = set1.union(set2)   # То же самое

# Пересечение
intersection1 = set1 & set2           # {3, 4}
intersection2 = set1.intersection(set2)  # То же самое

# Разность
difference1 = set1 - set2           # {1, 2}
difference2 = set1.difference(set2) # То же самое

# Симметричная разность (исключающее ИЛИ)
sym_diff1 = set1 ^ set2                    # {1, 2, 5, 6}
sym_diff2 = set1.symmetric_difference(set2)  # То же самое

# Проверки отношений
print(set1.isdisjoint(set2))    # False - есть общие элементы
print({1, 2}.issubset(set1))    # True - подмножество
print(set1.issuperset({1, 2}))  # True - надмножество
```

#### Методы множеств
```python
s = {1, 2, 3}

# Добавление элементов
s.add(4)           # {1, 2, 3, 4}
s.update([5, 6])   # {1, 2, 3, 4, 5, 6}
s.update({7, 8}, [9, 10])  # Можно передать несколько итерируемых

# Удаление элементов
s.remove(1)        # Удалить элемент (KeyError если нет)
s.discard(100)     # Удалить элемент (без ошибки если нет)
popped = s.pop()   # Удалить и вернуть произвольный элемент
s.clear()          # Очистить множество

# Копирование
original = {1, 2, 3}
copy_set = original.copy()
```

#### frozenset (Неизменяемые множества)
```python
# Создание
fs = frozenset([1, 2, 3, 4])
empty_fs = frozenset()

# Свойства
# - Неизменяемые (нельзя добавлять/удалять элементы)
# - Хешируемые (могут быть элементами других множеств или ключами словарей)
# - Поддерживают все операции чтения множеств

# Использование как ключи словаря
dict_with_frozenset_keys = {
    frozenset([1, 2]): 'first',
    frozenset([3, 4]): 'second'
}

# Множество множеств
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
```

---

## Специальные типы

### None (Пустое значение)
```python
# None - единственное значение типа NoneType
value = None
print(type(value))  # <class 'NoneType'>

# Проверка на None
if value is None:
    print("Значение пустое")

# Функции без return возвращают None
def no_return():
    pass

result = no_return()
print(result)  # None
```

### bytes и bytearray
```python
# bytes - неизменяемая последовательность байтов
b1 = b'hello'
b2 = bytes([72, 101, 108, 108, 111])  # То же самое
b3 = 'hello'.encode('utf-8')

print(b1[0])  # 104 (ASCII код 'h')

# bytearray - изменяемая последовательность байтов
ba = bytearray(b'hello')
ba[0] = 72  # Изменить первый байт
ba.append(33)  # Добавить байт (код '!')
print(ba.decode('utf-8'))  # Hello!

# Методы
print(b1.decode('utf-8'))     # Преобразовать в строку
print(b1.hex())               # Шестнадцатеричное представление
print(bytes.fromhex('48656c6c6f'))  # Создать из hex
```

### range (Диапазоны)
```python
# Создание
r1 = range(5)        # 0, 1, 2, 3, 4
r2 = range(1, 6)     # 1, 2, 3, 4, 5
r3 = range(0, 10, 2) # 0, 2, 4, 6, 8

# Свойства
print(len(r2))    # 5
print(r2.start)   # 1
print(r2.stop)    # 6
print(r2.step)    # 1

# Проверки
print(3 in r2)    # True
print(r2.index(3))  # 2
print(r2.count(3))  # 1

# Преобразование
list_from_range = list(r1)  # [0, 1, 2, 3, 4]
```

---

## Работа с типами

### Проверка типов
```python
# type() - точный тип
print(type(42))        # <class 'int'>
print(type([1, 2, 3])) # <class 'list'>

# isinstance() - проверка с учетом наследования
print(isinstance(42, int))     # True
print(isinstance(True, int))   # True (bool наследует от int)
print(isinstance(42, (int, float)))  # True (любой из типов)

# hasattr() - проверка наличия атрибута
print(hasattr([1, 2, 3], 'append'))  # True
print(hasattr(42, 'append'))         # False
```

### Преобразование типов
```python
# Явное преобразование
print(int('123'))      # 123
print(float('3.14'))   # 3.14
print(str(123))        # '123'
print(list('hello'))   # ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set([1, 2, 2, 3])) # {1, 2, 3}

# Неявное преобразование
print(1 + 2.0)   # 3.0 (int -> float)
print(True + 1)  # 2 (bool -> int)
```

### Получение информации о типах
```python
import sys

# Размер объекта в байтах
print(sys.getsizeof(42))      # Размер int
print(sys.getsizeof([1, 2, 3]))  # Размер списка

# Идентификатор объекта
a = [1, 2, 3]
b = a
print(id(a) == id(b))  # True - одинаковые объекты

# Все атрибуты и методы объекта
print(dir(42))  # Все методы числа
print(dir([]))  # Все методы списка

# Справка
help(list.append)  # Документация по методу
```

### Коллекции из модуля collections
```python
from collections import (
    defaultdict, Counter, OrderedDict, 
    deque, ChainMap, UserDict, UserList, UserString
)

# defaultdict - словарь с значениями по умолчанию
dd = defaultdict(list)
dd['key1'].append('value1')  # Автоматически создает список
print(dd)  # defaultdict(<class 'list'>, {'key1': ['value1']})

# Counter - подсчет элементов
counter = Counter('hello world')
print(counter)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(counter.most_common(2))  # [('l', 3), ('o', 2)]

# deque - двусторонняя очередь
dq = deque([1, 2, 3])
dq.appendleft(0)    # Добавить слева
dq.append(4)        # Добавить справа
print(dq)           # deque([0, 1, 2, 3, 4])
dq.popleft()        # Удалить слева
dq.pop()            # Удалить справа

# ChainMap - объединение словарей
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain = ChainMap(dict1, dict2)
print(chain['a'])   # 1 (ищет в порядке добавления)
```

---

## Полезные советы

### Выбор подходящей коллекции
- **list**: когда нужен порядок, индексирование, изменяемость
- **tuple**: когда нужна неизменяемость, можно использовать как ключ словаря
- **dict**: для быстрого поиска по ключу, когда нужны пары ключ-значение
- **set**: для уникальных элементов, быстрого поиска принадлежности, операций над множествами
- **deque**: когда часто добавляете/удаляете элементы с обеих сторон
- **defaultdict**: когда часто обращаетесь к несуществующим ключам словаря

### Производительность
```python
# Быстрые операции
# list: append(), pop(), доступ по индексу
# dict: доступ/изменение по ключу, in/not in
# set: add(), remove(), in/not in, операции множеств
# deque: appendleft(), popleft(), append(), pop()

# Медленные операции
# list: insert(0, x), pop(0), remove(), x in list (для больших списков)
# dict: сохранение порядка (хотя и гарантированно с Python 3.7+)
```

### Общие паттерны
```python
# Безопасная работа со словарями
data = {}
# Вместо if 'key' in data: data['key'].append(value)
data.setdefault('key', []).append(value)

# Объединение списков
lists = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in lists for item in sublist]
# Или с itertools.chain

# Группировка элементов
from itertools import groupby
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
grouped = {k: list(g) for k, g in groupby(data, key=lambda x: x[0])}

# Удаление дубликатов с сохранением порядка
def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]
```