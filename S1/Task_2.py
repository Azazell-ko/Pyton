# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2

n = int(input('Введите сколько машина проезжает киллометров за день - '))
m = int(input('Маршурт длинной - '))
days = m/n  #дни без округления 
resultat = int(- 1 * days // 1 * -1)    #округление числа в большую сторону, если есть остаток
print(resultat)
