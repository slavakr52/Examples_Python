
# n = 1.89         # простая печать
# print(n)


# n = "sdfgh"      # выделять можно любыми кавычками
# n1 = 'hgsh'
# print(n)

# n = 5            # type для вывода типа данных
# print (type (n), n)
# n1 = "dfhsd"
# print (type (n1), n1)

# n = "df\"gf"     # \ для вывода кавычек внутри строки
# print(n)
# n1 = 'sfg"adhsjh"'     
# print(n1)

# a = 5            # интерполяция
# b = 5.89
# c = 'hello'
# print(a,'-', b,'-',c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))

# print("Введите первую строку")    # ввод данных
# a = input()
# b = input("Введите вторую строку: ")
# c = a + b # 3 + 4 будет равно 34, чтобы нормально сложить читай дальше
# print(f"{a} + {b} = {c}") 

# c = 5.89            # типизация данных
# print(type(c), c)
# n = int(c)
# print(type(n), n)
# c = str(c)
# print(type(c), c)\

# c = 1                 #булево значение
# c = bool(c)
# print(type(c), c)

# v = 'dfgsdfg'         # надо самому понимать, что за тип данных указываешь
# v = int(v)

# a = int(input("Введите первое число: "))     # исправленный код из задачи выше
# b = int(input("Введите второе число: "))
# c = a + b
# print(f"{a} + {b} = {c}") 

# a = 5.89849             # округление числа
# b = 6.51651
# print(round(a*b, 3))

# iter = 2                # сокращённые присваивания
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 6 # iter = iter / 6
# iter //= 7 # iter = iter // 7
# iter %= 8 # iter = iter % 8
# iter **= 9 # iter = iter ** 9

# a = 20                    # оформление операторов ветвления
# b = 15
# if (a < 10):
#     print(a)
# else:
#     print(b)

# a = 20                    # связка операторо else-if
# b = 15
# c = 10
# d = 30
# if (b > a):                
#     print(b)
# elif (c > a):
#     print(c)
# else:
#     print(d)

# a = 13                    # логические операторы and, or
# b = 15
# c = 10
# if (b < a and c < a):
#     print("true")
# else: print("false")
#
# if (b < a or c < a):
#     print("true")
# else: print("false")

# n = int(input())            # поиск минимального делителя введённого числа
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

# x = range(0, 20, 3)         # range выдаёт значения из диапазона с шагом n
# for i in x:
#     print(i)

# a = "qwerty"                # for со строками
# for i in a:
#     print(i)

# line = ""                   # вложенные циклы
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = "Съешь ещё этих мягких французских булочек"
# print(len(text))             # длина строки
# print('ещё' in text)         # поиск по строке
# print(text.lower())          # все буквы в нижнем регистре
# print(text.upper())          # все буквы в верхнем регистре
# print(text.replace('ещё', 'ЕЩЁ'))   # меняет нужные символы в строке


