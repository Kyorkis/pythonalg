#В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.

import random
import numpy as np

arr_x = np.random.randint(-100,100,size=10)
print (arr_x)

m = -1
for i in range(0,len(arr_x)):    
    if arr_x[i] < 0 and m ==-1:
        m = i
    elif arr_x[i] < 0 and arr_x[i] > arr_x[m]:
        m = i
print(f'Наибольшее отрицательное число:{arr_x[m]}, его позиция: {m+1}')            



