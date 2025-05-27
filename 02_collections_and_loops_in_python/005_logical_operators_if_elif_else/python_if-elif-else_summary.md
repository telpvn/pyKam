# Условные конструкции if-elif-else в Python

## Базовый синтаксис

```python
if условие:
    # выполняется, если условие истинно
    действие_1
elif другое_условие:
    # выполняется, если первое условие ложно, а это истинно
    действие_2
else:
    # выполняется во всех остальных случаях
    действие_3
```

## 1. Простая конструкция if

```python
age = 18

if age >= 18:
    print("Вы совершеннолетний")

# Пример с числами
temperature = 25
if temperature > 20:
    print("На улице тепло")

# Пример с строками
name = "Анна"
if name == "Анна":
    print("Привет, Анна!")
```

## 2. Конструкция if-else

```python
age = 16

if age >= 18:
    print("Можно голосовать")
else:
    print("Пока нельзя голосовать")

# Проверка четности числа
number = 7
if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

# Проверка пустой строки
text = ""
if text:
    print(f"Текст: {text}")
else:
    print("Текст пустой")
```

## 3. Конструкция if-elif-else

```python
score = 85

if score >= 90:
    grade = "Отлично"
elif score >= 80:
    grade = "Хорошо"
elif score >= 70:
    grade = "Удовлетворительно"
elif score >= 60:
    grade = "Зачет"
else:
    grade = "Незачет"

print(f"Оценка: {grade}")
```

## 4. Множественные elif

```python
day = "понедельник"

if day == "понедельник":
    print("Начало рабочей недели")
elif day == "вторник":
    print("Вторник - день тяжелый")
elif day == "среда":
    print("Середина недели")
elif day == "четверг":
    print("Почти пятница")
elif day == "пятница":
    print("Ура! Пятница!")
elif day == "суббота":
    print("Выходной день")
elif day == "воскресенье":
    print("Воскресный отдых")
else:
    print("Неизвестный день")
```

## 5. Логические операторы в условиях

### Оператор and (И)
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Можете водить машину")
else:
    print("Не можете водить машину")

# Проверка диапазона
temperature = 22
if temperature >= 20 and temperature <= 25:
    print("Комфортная температура")
```

### Оператор or (ИЛИ)
```python
weather = "дождь"

if weather == "солнце" or weather == "облачно":
    print("Можно идти гулять")
else:
    print("Лучше остаться дома")

# Проверка выходных
day = "суббота"
if day == "суббота" or day == "воскресенье":
    print("Выходной день")
```

### Оператор not (НЕ)
```python
is_raining = False

if not is_raining:
    print("Дождя нет, можно гулять")
else:
    print("Идет дождь")

# Проверка на пустоту
my_list = []
if not my_list:
    print("Список пуст")
```

## 6. Сложные условия

```python
age = 20
student = True
income = 15000

if age < 25 and student and income < 20000:
    print("Скидка 50%")
elif age < 25 and not student:
    print("Скидка 20%")
elif age >= 65:
    print("Пенсионная скидка 30%")
else:
    print("Обычная цена")
```

## 7. Вложенные условия

```python
weather = "солнце"
temperature = 25

if weather == "солнце":
    if temperature > 20:
        print("Отличная погода для прогулки!")
    else:
        print("Солнечно, но прохладно")
else:
    if temperature > 15:
        print("Не солнечно, но тепло")
    else:
        print("Плохая погода")
```

## 8. Тернарный оператор (сокращенная запись)

```python
age = 20

# Полная запись
if age >= 18:
    status = "взрослый"
else:
    status = "несовершеннолетний"

# Сокращенная запись (тернарный оператор)
status = "взрослый" if age >= 18 else "несовершеннолетний"

# Еще примеры
number = 10
result = "четное" if number % 2 == 0 else "нечетное"

temperature = 30
clothing = "легкая одежда" if temperature > 25 else "теплая одежда"
```

## 9. Проверка истинности значений

```python
# Ложные значения в Python:
# False, 0, 0.0, "", [], {}, (), None

name = ""
if name:
    print(f"Привет, {name}!")
else:
    print("Имя не введено")

numbers = []
if numbers:
    print("В списке есть числа")
else:
    print("Список пуст")

value = None
if value:
    print(f"Значение: {value}")
else:
    print("Значение не задано")
```

## 10. Практические примеры

### Калькулятор скидок
```python
def calculate_discount(price, age, is_student, is_member):
    discount = 0
    
    if is_member:
        discount += 10
        
    if age < 18 or age >= 65:
        discount += 15
    elif is_student:
        discount += 10
        
    if discount > 25:
        discount = 25  # Максимальная скидка
        
    final_price = price * (1 - discount / 100)
    return final_price, discount

price, discount = calculate_discount(1000, 20, True, False)
print(f"Цена: {price}, Скидка: {discount}%")
```

### Определение сезона
```python
def get_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный месяц"

current_month = 6
season = get_season(current_month)
print(f"Месяц {current_month} - это {season}")
```

### Проверка пароля
```python
def check_password_strength(password):
    if len(password) < 8:
        return "Слабый пароль: слишком короткий"
    elif not any(c.isupper() for c in password):
        return "Слабый пароль: нет заглавных букв"
    elif not any(c.islower() for c in password):
        return "Слабый пароль: нет строчных букв"
    elif not any(c.isdigit() for c in password):
        return "Слабый пароль: нет цифр"
    else:
        return "Надежный пароль"

password = "MyPass123"
strength = check_password_strength(password)
print(strength)
```

## 11. Распространенные ошибки

### Неправильное использование ==
```python
# НЕПРАВИЛЬНО
age = 18
if age = 18:  # Ошибка! Это присваивание, а не сравнение
    print("18 лет")

# ПРАВИЛЬНО
if age == 18:
    print("18 лет")
```

### Сравнение с булевыми значениями
```python
is_active = True

# Избыточно
if is_active == True:
    print("Активен")

# Лучше
if is_active:
    print("Активен")

# Для отрицания
if not is_active:
    print("Неактивен")
```

### Проверка на None
```python
value = None

# НЕПРАВИЛЬНО
if value == None:
    print("Значение None")

# ПРАВИЛЬНО
if value is None:
    print("Значение None")

if value is not None:
    print("Значение задано")
```