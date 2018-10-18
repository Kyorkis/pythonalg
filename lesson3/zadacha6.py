#  В одномерном массиве найти сумму элементов,
#  находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.

import random
import numpy as np

arr_x = np.random.randint(-100,100,size=10)
print (arr_x)

i_max = 0
i_min = 0

for i in range(len(arr_x)):
    
    if arr_x[i] > arr_x[i_max]:
        i_max = i
    elif arr_x[i] < arr_x[i_min]:
        i_min = i 
        
print(arr_x[i_max],arr_x[i_min])      

x_summa=0

if i_max>i_min:
    for i in range (i_min+1,i_max):
        x_summa = x_summa + arr_x[i]
    print(f"Сумма чисел : {x_summa}")    


else:
    for i in range(i_max+1,i_min):
        x_summa = x_summa + arr_x[i]
    print(f"Сумма чисел : {x_summa}")    

