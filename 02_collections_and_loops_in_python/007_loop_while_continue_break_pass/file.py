# import time
#
# x = 1
# while True:
#     x += x
#     print(x)
#     time.sleep(1)
#
# print()

# x = 0
# #
# # while x < 6:
# #     print(f'Х равно {x}')
# #     x += 1
# #     time.sleep(0.5)
# # else:
# #     print('Завершено')

print()

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

summa = 0

for x in vals:
    if x % 2 == 0:
        continue
    else:
        summa += x
    if summa>10:
        break
print(summa)

print()

while True:
    pass
