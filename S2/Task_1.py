# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

n = int(input("Введите целое не отрицательное число "))
if n == 0:
    print("1")
i=1
factorial = 1
while i <= n:
    factorial = factorial * i
    i = i + 1
print('Итог', factorial)