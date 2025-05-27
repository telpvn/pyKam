a, b, c = 10, 20, 30,

print(a)
print(b)
print(c)

print()

a, b, c = 'string', 20, 3.14,

print(a)
print(b)
print(c)

print()

a, *b, c = 'string', 20, 3.14, 'Text', 30, 4.14

print(a)
print(b)
print(c)

print()

a, b, *c = 'string', 20, 3.14, 'Text', 30, 4.14

print(a)
print(b)
print(c)

print()

*a, b, c = 'string', 20, 3.14, 'Text', 30, 4.14

print(a)
print(b)
print(c)

print()

*a, b, c = [1, 2]

print(a)
print(b)
print(c)

print()

# Ошибка
# *a, b, c = [1]
#
# print(a)
# print(b)
# print(c)

print()

s = [4, 10]
print(list(range(*s)))


def func(a, b, c, d):
    print(a, b, c, d)


a = ('Hello', True, 78, [3, 4, 5])

func(*a)

print()


def func(*args):
    print(sum(args) * 0.06)

func()
