def printText():
    print('Hello world')


printText()
printText()
printText()

print()


def sqRing(p):
    s = 3.1415 * (p ** 2)
    print(s)


sqRing(10)

print()


def sqRing(p):
    s = 3.1415 * (p ** 2)
    return s


x = sqRing(20)
print(x)

print()

a = 30
print(sqRing(a))

print()


def getSquare(w, h):
    return 2 * (w + h)


print(getSquare(5, 5))


def printText(msq, end='!'):
    print(msq + end)


printText('Text')
printText('Text', '?')

print()


def printText(msq, end='!', sep=': '):
    print('Message' + sep + msq + end)


printText('Text')
printText('Text', '?')
printText('Text', '?', ' ')
printText('Text', sep='')

print()


def getSquare(w, h):
    return 2 * (w + h), w * h


print(getSquare(5, 5))
print(type(getSquare(5, 5)))

print()

a = True

if a:
    def sFunc(x, y, z):
        return print(x + y + z)
else:
    def sFunc(a, b, c):
        x = a + b / c
        print(x)

sFunc(10, 20, 30, )

print()


def funct(a, b, c):
    """

    :param a: Комент
    :param b: Переменная
    :param c:
    :return: Вывод
    """
    return a + b + c

help(funct)
