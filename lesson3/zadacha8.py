# Матрица 5x4 заполняется вводом с клавиатуры, 
# кроме последних элементов строк. Программа должна 
# вычислять сумму введенных элементов каждой строки и записывать 
# ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

import numpy as np

rows=4
cols=5
summa = 0

b = np.zeros((4,5))
print(b)

for i in range(rows):
    for j in range(cols-1):
        b[i][j]=input("Введите число")
        summa= summa+b[i][j]
    b[i][-1]=summa    
    print (b)
    summa =0




    