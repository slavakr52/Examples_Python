from random import randint
min = 0
max = 10000000

x = randint (min, max) # рандомное число



# метод последовательного перебора
count_perebor = 0
for i in range(min, max + 1):
    count_perebor += 1
    if i == x:
        print("Число найдено!")
        break

print ("Загаданное число было",x, "и для его поиска потребовалось" ,count_perebor, "итераций методом перебора")



# метод случайного отгадывания
count_random = 1
y = randint(min, max)

while x!=y:
    y = randint(min,max)
    count_random += 1

print ("Загаданное число было",x, "и для его поиска потребовалось" ,count_random, "итераций методом случайного отгадывания")



# метод бинарного поиска
count_bin = 1
y = (min + max)//2

while x!=y:
    count_bin += 1
    if x<y: 
        max = y - 1
    else: 
        min = y + 1
    y = (min + max) //2

print ("Загаданное число было",x, "и для его поиска потребовалось" ,count_bin, "итераций методом бинарного поиска")
