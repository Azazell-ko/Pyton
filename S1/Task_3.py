# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

a = int(input('Учеников в первом классе - '))
b = int(input('Учеников во втором классе - '))
c = int(input('Учеников в третьем классе - '))
result = (a+1) // 2 + (b+1) // 2 + (c+1) // 2
print(f"-> Наименьшее требуемое количество парт ", result)

# print(int(-1 * (a/2) // 1 * -1) + int(-1 * (b/2) // 1 * -1) + int(-1 * (c/2) // 1 * -1)) # сокращённый ответ
'''  
a1 = int(-1 * (a/2) // 1 * -1)
b1 = int(-1 * (b/2) // 1 * -1)
c1 = int(-1 * (c/2) // 1 * -1)
print(a1+b1+c1) # развёрнутый ответ
'''
# result = (
#   (a // 2 + (a % 2 ! = 0)) + (b // 2 + (b % 2 != 0)) + (c // 2 + (c % 2 != 0))
# )
# print(f"-> Наименьшее требуемое количество парт ", result)
"""

"""