#По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# number = int(input('Введите число: '))
# i = 1
# fact = 1
# while i <= number:
#     fact = fact * i
#     i += 1
# print(f'Факториал числа {number} равен {fact}')



# Дано натуральное число A > 1. 
# Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите 
# такое число n, что φ(n)=A. Если А не является 
# числом Фибоначчи, выведите число -1.

# count_number = int(input('Введите количество чисел Фибоначчи, среди которых будет осуществлён поиск: '))
# input_number = int(input('Введите число, которое мы сравним с числом Фибоначчи: '))
# number1 = 0
# number2 = 1
# if number1 == input_number: print('Это 1 по счёту число Фибоначчи')
# if number2 == input_number: print('Это 2 по счёту число Фибоначчи')
# fibo = number1 + number2
# for i in range(30):
#     fibo = number1 + number2
#     if fibo == input_number and fibo !=1:
#         print(f'Это {i+3} по счёту число Фибоначчи')
#         break
#     number1 = number2
#     number2 = fibo
# else: print(f'Среди первых {count_number} чисел Фибоначчи нет числа {input_number}')



# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает 
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит 
# N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса 
# соответствующего арбуза. Все числа натуральные и не превышают 30000.
import random

watermelon_count = int(input('Введите количество арбузов: '))
max = 0
min = 30000
for i in range (1, watermelon_count + 1):
    weight = random.randint(1, 30000)
    print(weight)
    if weight < min:
        min = weight
    if weight > max:
        max = weight
print(f'Самый лёгкий арбуз - {min}, самый тяжёлый арбуз - {max}')
