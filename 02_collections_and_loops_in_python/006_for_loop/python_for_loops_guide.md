# Циклы for в Python: Полное руководство

## 1. Основы цикла for

Цикл `for` позволяет перебирать элементы любого итерируемого объекта (списки, строки, кортежи, словари и др.).

### Базовая синтаксис:
```python
for переменная in итерируемый_объект:
    # действия с переменной
```

## 2. Примеры использования

### Перебор списка:
```python
fruits = ['яблоко', 'банан', 'апельсин']
for fruit in fruits:
    print(f"Мне нравится {fruit}")
```

### Перебор строки:
```python
word = "Python"
for letter in word:
    print(letter)
```

### Использование range():
```python
# Числа от 0 до 4
for i in range(5):
    print(i)

# Числа от 1 до 10
for i in range(1, 11):
    print(i)

# Числа с шагом 2
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

## 3. Работа со словарями

```python
student = {'имя': 'Анна', 'возраст': 20, 'курс': 2}

# Перебор ключей
for key in student:
    print(key)

# Перебор значений
for value in student.values():
    print(value)

# Перебор пар ключ-значение
for key, value in student.items():
    print(f"{key}: {value}")
```

## 4. Полезные функции с циклами

### enumerate() - получение индекса и значения:
```python
colors = ['красный', 'синий', 'зеленый']
for index, color in enumerate(colors):
    print(f"{index}: {color}")
```

### zip() - одновременный перебор нескольких списков:
```python
names = ['Алиса', 'Боб', 'Карл']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} - {age} лет")
```

## 5. Условия в циклах

### if-elif-else внутри цикла:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} - четное")
    else:
        print(f"{num} - нечетное")
```

### Условие с continue и break:
```python
for i in range(10):
    if i == 3:
        continue  # пропустить итерацию
    if i == 7:
        break     # выйти из цикла
    print(i)
```

## 6. Вложенные циклы

```python
# Таблица умножения
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")
    print("---")
```

## 7. Списковые включения (List Comprehensions)

Краткая форма создания списков с циклом:

```python
# Обычный способ
squares = []
for x in range(5):
    squares.append(x**2)

# С помощью спискового включения
squares = [x**2 for x in range(5)]

# С условием
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

## 8. Практические примеры

### Подсчет элементов:
```python
text = "программирование"
count = {}
for char in text:
    count[char] = count.get(char, 0) + 1
print(count)
```

### Фильтрация списка:
```python
numbers = [1, -2, 3, -4, 5, -6]
positive = []
for num in numbers:
    if num > 0:
        positive.append(num)
```

### Суммирование:
```python
prices = [100, 250, 75, 300]
total = 0
for price in prices:
    total += price
print(f"Общая сумма: {total}")
```

## 9. Советы по использованию

1. **Используйте осмысленные имена переменных** в циклах
2. **Избегайте изменения списка** во время его перебора
3. **Используйте enumerate()** когда нужен индекс элемента
4. **Рассмотрите списковые включения** для простых операций
5. **Помните о break и continue** для управления циклом

## 10. Частые ошибки

```python
# НЕПРАВИЛЬНО - изменение списка во время перебора
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # Может пропустить элементы!

# ПРАВИЛЬНО - создание нового списка
items = [1, 2, 3, 4, 5]
new_items = []
for item in items:
    if item % 2 != 0:
        new_items.append(item)
```