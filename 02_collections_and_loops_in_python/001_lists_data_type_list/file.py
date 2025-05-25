new_list = [1, 2, 3, 4]
mix_list = [12, 3.14, 'text']
print(len(new_list))
print(new_list[0])
print(new_list[-1])
print(new_list[2:])

print()

list_1 = ['anna', 'alex', 'max']
list_2 = ['john', 'nicolas', 'vlad']
print(list_1 + list_2)
list_1[0] = 'artur'
print(list_1)
list_1.append('anna')
print(list_1)
list_1.insert(1, 'john')
print(list_1)
print(list_1.index('max'))
print(list_1.index('max', 0, 10))
pop_del = list_1.pop()
print(pop_del)
print(list_1)
list_1.pop(0)
print(list_1)
list_1.clear()
print(list_1)

print()

list_3 = ['33', '22', '11', '44']
print(list_3)
list_3.sort()
print(list_3)
list_3.sort(reverse=True)
print(list_3)

print()

list_4 = ['abcde', 'bcb', 'da', 'cde', 'ser', 'q']
print(list_4)
list_4.sort()
print(list_4)
list_4.sort(key=len)
print(list_4)
list_4.reverse()
print(list_4)
