# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, 
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

n = int(input("Введите число ")) # 0 1 1 2 3 5 8 13 21 
c=0
k=1
i=1
while i<n+2:
     m=k+c
     k=c
     c=m
     i=i+1
     if m==n:
             print(i)
             break
else: print("-1")