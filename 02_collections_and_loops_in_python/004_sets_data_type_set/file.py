first_set = {'Alex', 'John', 'Georg', 'Alex'}
print(type(first_set))
print(first_set)
print(len(first_set))
first_set.add('Maxim')
print(first_set)
print('Maxim' in first_set)
first_set.remove('Alex')
print(first_set)
first_set.clear()
print(first_set)
first_set = {'Alex', 'John', 'Georg', 'Alex'}
second_set = {'Anton', 'Tom', 'Anna', 'Alex'}
third_set = first_set.union(second_set)
print(third_set)
fourth_set = first_set.intersection(second_set)
print(fourth_set)
fifth_set = first_set.difference(second_set)
print(fifth_set)
print(fifth_set - second_set)

print()

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set1[0])
