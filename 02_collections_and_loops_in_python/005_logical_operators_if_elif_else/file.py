"""
if True:
    print('True')
elif True:
    print('True')
else:
    print('Else')
"""

print('Введите число от 1 до 10')
x = int(input())

if x < 4:
    print('Число меньше 4-х')
elif x == 5:
    print('Число равно 5')
elif 10 > x > 6:
    if 8 > x > 6:
        print('Число 7')
    elif 9 > x > 7:
        print('Число 8')
    else:
        print('Число 9')
else:
    print('??? Введите корректное число')
