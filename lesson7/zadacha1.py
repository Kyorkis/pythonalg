# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
#  заданный случайными числами на промежутке [-100; 100). 
# Вывести на экран исходный и отсортированный массивы.


import random
import numpy as np

arr_x = np.random.randint(-100,100,10)

print(f"Исходный массив чисел-->{arr_x}")

n = 1

while n<len(arr_x):
    for i in range(len(arr_x)-n):
        if arr_x[i]<arr_x[i+1]:
            arr_x[i],arr_x[i+1]=arr_x[i+1],arr_x[i]

    n+=1

print(f"Отсортированный массив-->{arr_x}")





