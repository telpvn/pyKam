numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in numbers:
    print(i)

print()

numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in numbers:
    print(i * i)

print()

numbers = range(1, 100)
print(numbers)

new_list = []

for i in numbers:
    new_list.append(i)

print(new_list)

print()

for i in range(1, 16):
    if i % 2 == 0:
        print(f'{i} четное число')
    else:
        print(f'{i} не четное число')

print()

numbers = [1, 2, 3, 4, 5]

for x, item in enumerate(numbers):
    numbers[x] += 10

print(numbers)

print()

name = 'Alex Johnson'

for x in name:
    print(x)

print()

for _ in range(1, 15):
    print('Ошибка!!')

print()

some_tuple = (11, 'Alex', 3.14)

for x in some_tuple:
    print(x)

print()

some_list = [('John', 22), ('Alex', 33), ('Artem', 44)]

for (name, age) in some_list:
    print(f'{name} is {age} years old')

print()

some_dist = {
    'Alex': 111,
    'Maxim': 222,
    'Anna': 333
}

for x in some_dist.items():
    print(x)

print(type(x))

print()

for x, y in some_dist.items():
    print(f'Ключ {x} и Значение {y}')

print()

for value in some_dist.values():
    print(value)
