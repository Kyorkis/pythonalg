#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import numpy as np

array_x = np.random.randint(-500,500,size=15)

x_min = 0
i_min = 0
x_max = 0
i_max = 0
       
for i in range(0,len(array_x)-1):
    if array_x[i] > x_max:
        x_max = array_x[i]
        i_max = i
    elif array_x[i] < x_min:
        x_min = array_x[i]
        i_min = i

print(f"Старый массив --- {array_x}")
print(f"Индекс наибольшего - {i_max},число {x_max}; Наименьшего - {i_min}, число {x_min}")
array_x[i_max],array_x[i_min] = array_x[i_min],array_x[i_max]      
print(f"Новый массив --- {array_x}")        