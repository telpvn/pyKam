# Функции в Python: Основы

## 1. Конструкция функции

```python
def имя_функции(список_аргументов):
    """Документация функции (необязательно)"""
    # тело функции
    операторы
    return результат  # необязательно
```

### Пример простой функции

```python
def приветствие(имя):
    """Функция для приветствия пользователя"""
    сообщение = f"Привет, {имя}!"
    return сообщение

# Вызов функции
результат = приветствие("Анна")
print(результат)  # Привет, Анна!
```

## 2. Позиционные (неименованные) параметры

Параметры передаются в том порядке, в котором они определены в функции.

```python
def вычислить(a, b, c):
    результат = a + b * c
    return результат

# Вызов с позиционными аргументами
ответ = вычислить(1, 2, 3)  # a=1, b=2, c=3
print(ответ)  # 7

# Порядок важен!
ответ2 = вычислить(3, 2, 1)  # a=3, b=2, c=1
print(ответ2)  # 5
```

### Пример с разными типами данных

```python
def создать_профиль(имя, возраст, город):
    профиль = f"{имя}, {возраст} лет, живет в {город}"
    return профиль

пользователь = создать_профиль("Иван", 25, "Москва")
print(пользователь)  # Иван, 25 лет, живет в Москва
```

## 3. Параметры по умолчанию (дефолтные)

Можно задать значения по умолчанию для параметров.

```python
def поздороваться(имя, приветствие="Привет"):
    return f"{приветствие}, {имя}!"

# Использование значения по умолчанию
print(поздороваться("Мария"))  # Привет, Мария!

# Переопределение значения по умолчанию
print(поздороваться("Петр", "Добро пожаловать"))  # Добро пожаловать, Петр!
```

### Важно: мутабельные объекты по умолчанию

```python
# ❌ Неправильно - опасно!
def добавить_элемент(элемент, список=[]):
    список.append(элемент)
    return список

# ✅ Правильно
def добавить_элемент(элемент, список=None):
    if список is None:
        список = []
    список.append(элемент)
    return список

# Пример использования
новый_список = добавить_элемент("первый")
print(новый_список)  # ['первый']
```

### Множественные параметры по умолчанию

```python
def настроить_сервер(хост="localhost", порт=8000, отладка=False):
    конфиг = f"Сервер: {хост}:{порт}, отладка: {отладка}"
    return конфиг

# Разные способы вызова
print(настроить_сервер())  # localhost:8000, отладка: False
print(настроить_сервер("192.168.1.1"))  # 192.168.1.1:8000, отладка: False
print(настроить_сервер("localhost", 3000))  # localhost:3000, отладка: False
print(настроить_сервер("localhost", 3000, True))  # localhost:3000, отладка: True
```

## 4. Именованные параметры

Можно передавать аргументы по имени, независимо от порядка.

```python
def создать_отчет(заголовок, содержание, автор="Неизвестен"):
    отчет = f"""
    Отчет: {заголовок}
    Автор: {автор}
    Содержание: {содержание}
    """
    return отчет

# Именованные аргументы (порядок не важен)
отчет1 = создать_отчет(
    содержание="Анализ продаж за месяц",
    заголовок="Месячный отчет",
    автор="Аналитик Иванов"
)

# Смешивание позиционных и именованных
отчет2 = создать_отчет(
    "Квартальный отчет",  # позиционный
    содержание="Финансовые показатели",  # именованный
    автор="Бухгалтер Петрова"  # именованный
)

print(отчет1)
print(отчет2)
```

### Принудительно именованные параметры

```python
def рассчитать_стоимость(базовая_цена, *, налог=0.2, скидка=0):
    """* означает, что все параметры после него должны быть именованными"""
    итоговая_цена = базовая_цена * (1 + налог) * (1 - скидка)
    return итоговая_цена

# Правильно
цена = рассчитать_стоимость(1000, налог=0.18, скидка=0.1)
print(цена)  # 1062.0

# ❌ Это вызовет ошибку:
# цена = рассчитать_стоимость(1000, 0.18, 0.1)
```

## 5. Оператор return

`return` завершает выполнение функции и возвращает значение.

```python
def проверить_возраст(возраст):
    if возраст >= 18:
        return "Совершеннолетний"
    else:
        return "Несовершеннолетний"

статус = проверить_возраст(20)
print(статус)  # Совершеннолетний
```

### Множественные return

```python
def найти_максимум(числа):
    if not числа:
        return None  # Ранний выход
    
    максимум = числа[0]
    for число in числа[1:]:
        if число > максимум:
            максимум = число
    
    return максимум

результат = найти_максимум([3, 7, 2, 9, 1])
print(результат)  # 9
```

### Возвращение нескольких значений

```python
def статистика(числа):
    if not числа:
        return None, None, None
    
    минимум = min(числа)
    максимум = max(числа)
    среднее = sum(числа) / len(числа)
    
    return минимум, максимум, среднее

# Распаковка результата
мин, макс, сред = статистика([1, 2, 3, 4, 5])
print(f"Мин: {мин}, Макс: {макс}, Среднее: {сред}")  # Мин: 1, Макс: 5, Среднее: 3.0
```

## 6. Функции как объекты первого класса

В Python функции можно передавать как аргументы и присваивать переменным.

```python
def сложение(a, b):
    return a + b

def умножение(a, b):
    return a * b

def применить_операцию(x, y, операция):
    """Применяет переданную функцию к двум числам"""
    результат = операция(x, y)
    return результат

# Передача функции как аргумента
результат1 = применить_операцию(5, 3, сложение)
результат2 = применить_операцию(5, 3, умножение)

print(результат1)  # 8
print(результат2)  # 15
```

### Присваивание функций переменным

```python
def приветствие():
    return "Привет!"

# Присваиваем функцию переменной
моя_функция = приветствие

# Теперь можно вызывать через переменную
print(моя_функция())  # Привет!

# Функция и переменная ссылаются на один объект
print(приветствие is моя_функция)  # True
```

### Список функций

```python
def квадрат(x):
    return x ** 2

def куб(x):
    return x ** 3

def корень(x):
    return x ** 0.5

# Создаем список функций
математические_функции = [квадрат, куб, корень]

число = 4
for функция in математические_функции:
    результат = функция(число)
    имя_функции = функция.__name__
    print(f"{имя_функции}({число}) = {результат}")

# Вывод:
# квадрат(4) = 16
# куб(4) = 64
# корень(4) = 2.0
```

## Практические примеры

### Калькулятор с функциями

```python
def калькулятор(a, b, операция="+"):
    """Простой калькулятор"""
    if операция == "+":
        return a + b
    elif операция == "-":
        return a - b
    elif операция == "*":
        return a * b
    elif операция == "/":
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Неизвестная операция"

# Примеры использования
print(калькулятор(10, 5))        # 15 (сложение по умолчанию)
print(калькулятор(10, 5, "-"))   # 5
print(калькулятор(10, 5, "*"))   # 50
print(калькулятор(10, 5, "/"))   # 2.0
```

### Валидация данных

```python
def проверить_email(email, строгая_проверка=False):
    """Проверяет корректность email адреса"""
    if not email or "@" not in email:
        return False
    
    if строгая_проверка:
        # Более строгая проверка
        части = email.split("@")
        if len(части) != 2:
            return False
        локальная, домен = части
        if not локальная or not домен or "." not in домен:
            return False
    
    return True

# Тестирование
emails = ["test@example.com", "invalid-email", "user@domain", ""]

for email in emails:
    базовая = проверить_email(email)
    строгая = проверить_email(email, строгая_проверка=True)
    print(f"{email}: базовая={базовая}, строгая={строгая}")
```

## Основные принципы

1. **Одна функция - одна задача**: функция должна решать конкретную задачу
2. **Понятные имена**: название функции должно отражать её назначение
3. **Документация**: добавляйте docstring для сложных функций
4. **Возврат значений**: функция должна возвращать результат, а не только печатать
5. **Избегайте глобальных переменных**: передавайте данные через параметры

```python
def хорошая_функция(данные, настройка=True):
    """
    Обрабатывает данные согласно настройке.
    
    Args:
        данные: входные данные для обработки
        настройка: флаг включения дополнительной обработки
    
    Returns:
        обработанные данные
    """
    результат = данные.copy() if hasattr(данные, 'copy') else данные
    
    if настройка:
        # дополнительная обработка
        pass
    
    return результат
```