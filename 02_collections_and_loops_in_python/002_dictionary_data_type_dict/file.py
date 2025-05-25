students = {
    'alex': 258,
    'max': 227,
    'anna': 278
}
print(students)
print(students['anna'])
print(students.get('alex'))
students['andrey'] = 268
print(students)
students['andrey'] = 177
print(students)
students.setdefault('oleg')
print(students)
students.pop('oleg')
print(students)
print(students.keys())
print(type(students.keys()))
key_list = list(students.keys())
print(key_list)
print(type(key_list))
print(students.values())
print(type(students.values()))
print('anna' in students)
print('peter' not in students)
