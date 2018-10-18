#В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
import numpy as np

arr_x = np.random.randint(-1000,1000,size=10)
print (arr_x)

x_min = arr_x[0]
x2_min = arr_x[0]

for i in range(len(arr_x)):
    if arr_x[i] < x_min:
        x_min = arr_x[i] 

for i in range(len(arr_x)):
    if arr_x[i] < x2_min and arr_x[i] > x_min:
        x2_min = arr_x[i]
print (f"Самое маленькое число:{x_min}, второе минимальное :{x2_min}")        