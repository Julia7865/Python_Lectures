# def f(x):
#     return x**2

# g = f
# print(f(4))
# print(g(4))
# print(type(f))
# print(type(g))


# def calc(x):
#     return x + 10
# print(calc(10))

# def calc2(x):
#     return x*10
# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc, 10)


# def sum(x, y):
#     return x + y
# sum = lambda x, y: x + y

# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a,b)

# calc(lambda x, y: x + y, 4, 5)


### List Comprehension

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# list = []

# for i in range(1, 101):
#     if (i% 2 == 0):
#         list.append(i)

# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 100) if i % 2 ==0]
# print(list)


### Анонимные, lambda функции

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 28'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2, res))
# print(res)

### Функция map

# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#          ↓  ↓  ↓  ↓  ↓
#       [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int,input().split()))
# print(data)


# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


### Функция filter

# Функция filter() применяет указанную функцию к каждому элементу итерируемого обьекта 
# и возвращает итератор с теми обьектами, для которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#                 ↓
#              [ 2, 4 ]
# Нельзя пройтись дважды

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)



# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


### Функция zip

# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора

# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]

# Нельзя пройтись дважды

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)

### Функция enumerate

# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.

# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#                               ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(enumerate(ids))
# print(data)