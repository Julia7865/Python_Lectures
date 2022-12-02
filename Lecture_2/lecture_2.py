# Данные, функции модули в Python

# Данные

# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')  # открыть файл file.txt для добавления
# data.writelines(colors)   # записать данные, разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close() # закрытие подключения к файлу


# with open('file.txt', 'a') as data:
#     data.write('line 11111\n')
#     data.write('line 22222\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# Функции

# import Lecture_1 as l

# print(l.f(1))


# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))     # ошибка


# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))     # !!!
# print(new_string(4))       # 12 3*4


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))    # asdw
# print(concatenatio('a', '1'))     # a1
# # print(concatenatio(1, 2, 3, 4))   # TypeError: ...


# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)   # 1 1 2 3 5 8 13 21 34


# Кортежи

# t = ()
# print(type(t))     # tuple
# t = (1,)
# print(type(t))     # tuple
# t = (1)
# print(type(t))     # int
# t = (28, 9, 1990)
# print(type(t))     # tuple
# colors = ['red', 'green', 'blue']
# print(colors)      # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)           # ['red', 'green', 'blue']

# t = tuple(['red', 'green', 'blue'])
# print(t[0])       # red
# print(t[2])       # blue
# print(t[10])    # IndexError: tuple index out of range
# print(t[-2])      # green
# print(t[-200])  # IndexError: tuple index out of rang

# for e in t:
#     print(e)      # red green blue
# t[0] = 'black'    # кортеж неизменяем


# Распаковка кортежа

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue


# Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': '!',
#         'left': '-',
#         'down': '@',
#         'right': '>'
#     }
# print(dictionary)         # {'up': '!', 'left': '-', 'down': '@', 'right': '>'}
# print(dictionary['left']) # -

# for k in dictionary.keys():    # выводит ключи
#     print(k)
# for k in dictionary.values():    # выводит значения
#     print(k)


# print(dictionary['up'])   # !
# типы ключей могут отличаться 

# dictionary['left'] = '<'
# print(dictionary['left'])    # <
# print(dictionary['type'])  # Ключ отсутствует
# del dictionary['left']       # удаление элемента

# for item in dictionary:     # for (k, v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))


# Множества

# colors = {'red', 'green', 'blue'}
# print(colors)    # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)    # {'red', 'green', 'blue'} не добавилось, потому что оно уже есть 
# colors.add('gray')
# print(colors)    # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors)    # {'green', 'blue', 'gray'}
# # colors.remove('red')    # KeyError: 'red'
# colors.discard('red')     # ok
# print(colors)    # {'green', 'blue', 'gray'}
# colors.clear()   # { }


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()           # c = {1, 2, 3, 5, 8}
# u = a.union(b)         # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)  # i = {8, 2, 5}
# dl = a.difference(b)   # dl = {1, 3}
# dr = b.difference(a)   # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}

# s = frozenset(a)    # замораживает множество, нельзя вносить изменения



# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

list1 = [1, 2, 3, 4, 5]

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop(2))
# print(list1)
# print(list1.pop())
# print(list1)

print(list1.insert(2, 11))   # добавляет элемент на указанную позицию
print(list1)

print(list1.append(11))   # добавляет 11 в конец
print(list1)