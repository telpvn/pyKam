# Множества в Python - Краткий справочник

## 1. Что такое множество (set)
Множество - это коллекция **уникальных объектов**. В множестве не может быть повторяющихся элементов.

```python
# Основные характеристики:
# ✅ Уникальные элементы (дубликаты автоматически удаляются)
# ✅ Изменяемое (можно добавлять/удалять элементы)
# ❌ Неупорядоченное (нет индексов)
# ❌ Не поддерживает обращение по индексу
```

## 2. Создание множества
```python
# Синтаксис - фигурные скобки
s = {1, 2, 3, 4}
colors = {'красный', 'синий', 'зеленый'}
mixed = {1, 'текст', 3.14}

# Создание из списка (дубликаты удалятся)
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)  # {1, 2, 3, 4}

# Создание из строки
letters = set('привет')  # {'п', 'р', 'и', 'в', 'е', 'т'}

# Пустое множество (НЕ {}, это словарь!)
empty_set = set()
```

## 3. Добавление элементов - add()
```python
fruits = {'яблоко', 'банан'}

# Добавление одного элемента
fruits.add('апельсин')
print(fruits)  # {'яблоко', 'банан', 'апельсин'}

# Попытка добавить существующий элемент (ничего не произойдет)
fruits.add('яблоко')
print(fruits)  # {'яблоко', 'банан', 'апельсин'} - без изменений
```

## 4. Удаление элементов - remove()
```python
numbers = {1, 2, 3, 4, 5}

# Удаление элемента (если его нет - ошибка)
numbers.remove(3)
print(numbers)  # {1, 2, 4, 5}

# numbers.remove(10)  # KeyError! Элемента нет

# Безопасное удаление - discard()
numbers.discard(4)     # Удалит 4
numbers.discard(10)    # Ничего не произойдет, ошибки не будет
```

## 5. Очистка множества - clear()
```python
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)  # set() - пустое множество
```

## 6. Объединение множеств - union()
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Объединение (все уникальные элементы)
result = set1.union(set2)
print(result)  # {1, 2, 3, 4, 5}

# Альтернативный синтаксис с оператором |
result2 = set1 | set2
print(result2)  # {1, 2, 3, 4, 5}

# Объединение нескольких множеств
set3 = {6, 7}
all_sets = set1.union(set2, set3)  # {1, 2, 3, 4, 5, 6, 7}
```

## 7. Пересечение множеств - intersection()
```python
students_math = {'Анна', 'Петр', 'Мария', 'Иван'}
students_physics = {'Петр', 'Мария', 'Елена', 'Андрей'}

# Пересечение (общие элементы)
both_subjects = students_math.intersection(students_physics)
print(both_subjects)  # {'Петр', 'Мария'}

# Альтернативный синтаксис с оператором &
both_subjects2 = students_math & students_physics
print(both_subjects2)  # {'Петр', 'Мария'}
```

## 8. Разность множеств - difference()
```python
all_students = {'Анна', 'Петр', 'Мария', 'Иван', 'Елена'}
absent_today = {'Петр', 'Елена'}

# Разность (элементы первого, исключая второе)
present_today = all_students.difference(absent_today)
print(present_today)  # {'Анна', 'Мария', 'Иван'}

# Альтернативный синтаксис с оператором -
present_today2 = all_students - absent_today
print(present_today2)  # {'Анна', 'Мария', 'Иван'}
```

## 9. Проверка подмножества - issubset()
```python
small_set = {1, 2}
big_set = {1, 2, 3, 4, 5}

# Является ли первое множество подмножеством второго?
is_subset = small_set.issubset(big_set)
print(is_subset)  # True

# Альтернативный синтаксис
is_subset2 = small_set <= big_set
print(is_subset2)  # True

# Проверка примеров
colors = {'красный', 'синий'}
primary_colors = {'красный', 'синий', 'желтый'}
print(colors.issubset(primary_colors))  # True
```

## 10. Проверка надмножества - issuperset()
```python
big_set = {1, 2, 3, 4, 5}
small_set = {2, 3}

# Является ли первое множество надмножеством второго?
is_superset = big_set.issuperset(small_set)
print(is_superset)  # True

# Альтернативный синтаксис
is_superset2 = big_set >= small_set
print(is_superset2)  # True

# Пример: все ли студенты группы есть в общем списке?
group_a = {'Анна', 'Петр'}
all_students = {'Анна', 'Петр', 'Мария', 'Иван'}
print(all_students.issuperset(group_a))  # True
```

## 11. Множества НЕ поддерживают индексацию
```python
my_set = {1, 2, 3, 4, 5}

# Это НЕ работает:
# element = my_set[0]  # TypeError!

# Для доступа к элементам используйте:
for element in my_set:
    print(element)

# Или преобразуйте в список:
my_list = list(my_set)
first_element = my_list[0]  # Теперь работает
```

## Дополнительные операции

### Проверка наличия элемента
```python
fruits = {'яблоко', 'банан', 'апельсин'}

if 'яблоко' in fruits:
    print("Яблоко есть в множестве")

if 'груша' not in fruits:
    print("Груши нет в множестве")
```

### Длина множества
```python
numbers = {1, 2, 3, 4, 5}
count = len(numbers)  # 5
```

### Симметричная разность
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Элементы, которые есть в одном из множеств, но не в обоих
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # {1, 2, 4, 5}

# Альтернативный синтаксис
sym_diff2 = set1 ^ set2
print(sym_diff2)  # {1, 2, 4, 5}
```

### Копирование множества
```python
original = {1, 2, 3}
copy = original.copy()
```

## Практические применения

### Удаление дубликатов из списка
```python
numbers_with_duplicates = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(unique_numbers)  # [1, 2, 3, 4, 5]
```

### Поиск общих элементов
```python
list1 = ['a', 'b', 'c', 'd']
list2 = ['c', 'd', 'e', 'f']
common = set(list1) & set(list2)
print(common)  # {'c', 'd'}
```

### Проверка уникальности
```python
def has_duplicates(items):
    return len(items) != len(set(items))

data = [1, 2, 3, 2]
print(has_duplicates(data))  # True
```