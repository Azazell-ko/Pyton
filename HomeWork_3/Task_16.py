# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите количество чисел '))
list = []  # так же можно x = list()
for i in range(n):
    list.append(int(input('Введите числа ')))
b = int(input('Введите искомое число '))    
count = 0 
for i in range(len(list)):
    if list[i] == b:
        count = count + 1
print(count)