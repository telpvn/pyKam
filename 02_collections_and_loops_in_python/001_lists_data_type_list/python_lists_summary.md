# Списки в Python - Краткий справочник

## 1. Создание списка
```python
# Синтаксис
spisok = [element1, element2, element3]

# Примеры
numbers = [1, 2, 3, 4, 5]
fruits = ['яблоко', 'банан', 'апельсин']
mixed = [1, 'текст', 3.14, True]
```

## 2. Обращение по индексу
```python
spisok = ['a', 'b', 'c', 'd']
print(spisok[0])    # 'a' - первый элемент
print(spisok[-1])   # 'd' - последний элемент
print(spisok[1])    # 'b' - второй элемент
```

## 3. Срезы (slicing)
```python
spisok = [0, 1, 2, 3, 4, 5]
print(spisok[0:3])   # [0, 1, 2] - элементы с 0 по 2
print(spisok[2:])    # [2, 3, 4, 5] - с 2 до конца
print(spisok[:3])    # [0, 1, 2] - с начала до 2
print(spisok[::2])   # [0, 2, 4] - каждый второй элемент
```

## 4. Добавление элементов - append()
```python
spisok = [1, 2, 3]
spisok.append(4)     # Добавляет в конец
print(spisok)        # [1, 2, 3, 4]
```

## 5. Вставка элементов - insert()
```python
spisok = [1, 2, 4]
spisok.insert(2, 3)  # Вставляет 3 на позицию 2
print(spisok)        # [1, 2, 3, 4]
```

## 6. Поиск индекса - index()
```python
spisok = ['a', 'b', 'c', 'b']
index = spisok.index('b')  # Возвращает 1 (первое вхождение)
print(index)
```

## 7. Удаление элементов - pop()
```python
spisok = [1, 2, 3, 4]
last = spisok.pop()      # Удаляет и возвращает последний: 4
second = spisok.pop(1)   # Удаляет и возвращает элемент с индексом 1
print(spisok)            # [1, 3]
```

## 8. Очистка списка - clear()
```python
spisok = [1, 2, 3, 4, 5]
spisok.clear()           # Удаляет все элементы
print(spisok)            # []
```

## 9. Сортировка - sort()
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()           # Сортирует по возрастанию
print(numbers)           # [1, 1, 3, 4, 5]

# Сортировка по убыванию
numbers.sort(reverse=True)
print(numbers)           # [5, 4, 3, 1, 1]
```

## 10. Переворот списка - reverse()
```python
spisok = [1, 2, 3, 4, 5]
spisok.reverse()         # Переворачивает порядок элементов
print(spisok)            # [5, 4, 3, 2, 1]
```

## Дополнительные полезные операции

### Длина списка
```python
spisok = [1, 2, 3, 4, 5]
length = len(spisok)     # 5
```

### Проверка наличия элемента
```python
spisok = [1, 2, 3, 4, 5]
if 3 in spisok:
    print("Элемент найден")
```

### Копирование списка
```python
original = [1, 2, 3]
copy1 = original.copy()        # Метод copy()
copy2 = original[:]            # Срез
copy3 = list(original)         # Конструктор list()
```