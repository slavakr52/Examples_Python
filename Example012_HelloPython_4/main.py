# def f(x):
#     return x*x
# a = f
# print(a(5))
# print(f(5))

#==================================
# def calc1(a, b):
#     return a + b

# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calc1, 5, 5)

#==================================
# calc1 = lambda a, b: a + b  # лямбда-функция

#==================================
# В списке хранятся числа. Нужно выбрать только четные и 
# составить список пар
# list = [1, 2, 3, 5, 8, 15, 23, 38]
# list2 = []
                             # мой вариант решения
# for i in list:
#     if i % 2 == 0:
#         list2.append(f'({i}, {i*i})')
# print(list2)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:             # лекционный вариант 1
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)             # лекционный вариант 2
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)

#==================================
# list_1 = [x for x in range(1,20)]
# print(list_1)
#                      # функция map делает что-то из первого аргумента со всеми объектами второго аргумента
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# data = '1 2 3 5 8 15 23 38'
# print(data)                        # пример
# data = list(map(int, data.split()))
# print(data)

# data = [1, 2, 3, 5, 8, 15, 23, 38]    #функция filter ищет элементы по условию в аргументе 1
# res = list(filter(lambda x: x % 10 == 5, data))      # в объектах аргумента 2
# print(res)

#==================================

# ещё есть функции zip и enumerate







