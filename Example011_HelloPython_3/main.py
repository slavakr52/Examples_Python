# def sum_numbers(n):  # выдаёт сумму чисел от 1 до n
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum

# a = sum_numbers(5)
# print(a)



# def sum_str(*args):   # звёздочкой передаём неограниченное кол-во элементов
#     res = ''
#     for i in args:
#         res+=i
#     return res

# print(sum_str('q','w'))



# import module        # импорт функции

# print(module.max1(5,9))


# def fib(n):          # рекурсия (фибоначчи)
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list = []
# for i in range(1,10):
#     list.append(fib(i))
# print(list)



# def quick_sort(array):      # быстрая сортировка
#     if len(array) < 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([24,5,6,3,6,1,2,9,6,54]))


# def merge_sort(nums):      # сортировка слиянием
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else: 
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list = [6,4,7,78,8,4,54,3434,6,767,7,74,547,5,4,3,3,6,7,567,568]
# merge_sort(list)
# print(list)
    


