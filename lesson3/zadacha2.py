#Во втором массиве сохранить индексы четных элементов первого массива.
#  Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив 
# надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля), 
# т.к. именно в этих позициях первого массива стоят четные числа.



#Сама функция --- type = <class 'function'>, size = 72, object = <function func at 0x00C308A0>

#type = <class 'list'>, size = 92, object = [8, 56, -186, 65, -10, 11, 15, -17, 19, 859, 110, 111, 954, -85]
#type = <class 'list'>, size = 36, object = [] (оба пока пустые) 
#Система win 10 64 

import sys

array_x = [8,56,-186,65,-10,11,15,-17,19,859,110,111,954,-85,]
array_q = []
array_c = []
def func(array_x,array_q,array_c):
   
    for i in array_x:
        if i%2==0:  

            array_q.append(i)

    
             

    for i in range(0,len(array_x)-1):

        if array_x[i]%2==0:
            array_c.append(i)   
    return(f'Индексы четных чисел - {array_c}'),(f'Четные числа - {array_q}')      
print(func([8,56,-186,65,-10,11,15,-17,19,859,110,111,954,-85,],[],[]))



def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')


show_size(func)                
show_size(array_x)
show_size(array_q)
show_size(array_c)