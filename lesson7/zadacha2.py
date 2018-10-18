#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50).
#  Выведите на экран исходный и отсортированный массивы.


import numpy as np
import random

list_x = np.random.randint(0,50,10)

print(f"Старый список-->{list_x}")


def merge_sort(list_x):
    n = len(list_x)
    if n <2:
        return list_x

    lft= merge_sort(list_x[:n//2])
    rgt= merge_sort(list_x[n//2:n])

    i,j = 0,0
    res =[]
    while i <len(lft) or j < len(rgt):
        if not i <len(lft):
            res.append(rgt[j])
            j+=1
        elif not j<len(rgt):
            res.append(lft[i])
            i+=1
        elif lft[i] < rgt[j]:
            res.append(lft[i])
            i+=1
        else:
            res.append(rgt[j])
            j+=1            
    return res

print(f"Отсортированный массив-->{merge_sort(list_x)}")    