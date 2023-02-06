# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# d g h t r g r h t j h b v f d s d f

# d g h t r g_2 r_2 h_2 t_2 j h_3 b v f d_2 s d_3 f_2

# string = "d g h t r g r h t j h b v f d s d f"
# list = string.split()

# new_list = []
# dict = {}

# for letter in list:
#     dict[letter] = dict.get(letter, 0) + 1
#     if dict.get(letter) > 1:
#         new_list.append(letter + '_' + str(dict.get(letter)))
#     else:
#         new_list.append(letter)

# print(' '.join(new_list))



# str = "d g h t r g r h t j h b v f d s d f".split()
# for i in range(len(str)):
#     k = 1
#     for j in range(i + 1, len(str)):
#         if str[i] == str[j]:
#             k += 1         
#             str[j] = f'{str[j]}_{k}'
# print(*str)


# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.

# string = input('Введите слова через пробел: ')
# print(f'Различных слов в тексте: {len(set(string.split()))}')

# Дана последовательность чисел. Получить список 
# уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# list = [1, 2, 3, 5, 1, 5, 3, 10]
# dict = {}

# for number in list:
#     dict[number] = dict.get(number, 0) + 1
#     if dict.get(number) > 1:
#         del dict[number]

# new_list = []

# for key, value in dict.items():
#     new_list.append(key)

# print(new_list)         # лучше использовать list.count
