# Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на 
# максимальные. Напишите программу, которая заменяет 
# оценки Василия, но наоборот: все максимальные – на минимальные.

from random import randint as rnd

list = []
for i in range(10):
    list.append(rnd(2, 5))
print(list)

for i in range(len(list)):
    max = 2
    min = 5
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]

for i in range(len(list)):
    if list[i] == max:
        list[i] = min
print(list)
