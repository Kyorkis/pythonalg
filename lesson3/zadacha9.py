#Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import numpy as np
import random

rows = 5
cols = 5
mass = []

mass = np.random.randint(10,100, size=(5,5))
print(mass)
min_col=10
min_abs=10

for j in range(cols):
    min_col = 100
    for i in range(rows):

        if mass[i][j] < min_col:
            min_col=mass[i][j]

    if min_col > min_abs:
        min_abs=min_col    
        
print (f"Максимальное число из минимальных в столбцах данной матрицы ---{min_abs}")            
        


