#За день машина проезжает n километров. 
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# import math

# n = 700
# m = 750
# print(math.ceil(m / n))

#======================================================

#Дано натуральное число. Требуется определить, 
# является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, 
# иначе выведите NO. Напомним, что в соответствии 
# с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также 
# если он кратен 400.

# year = int(input("Проверка года на високосность, введите год: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

#=======================================================

#Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

number = float(input("Введите число: "))
if (number % 2 == 0):
    print('НЕТ')
else:   
    print(int((number*10) % 10))