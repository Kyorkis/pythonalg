#Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ... Количество элементов (n) вводится с клавиатуры.

n = input('Введите количество элементов последовательности(1, -0.5, 0.25, -0.125, ...):')
n = int(n)

element = 1
summa=0
i = 0 
while i<n:
    summa = summa + element
    element = element /-2
    i +=1

print(f'Сумма {n} элементов последовательности , равняется {summa}')




