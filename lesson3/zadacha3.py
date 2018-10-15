#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# type= <class 'numpy.int32'>, size = 16,object = 58 (x_max в итераторе)
# type= <class 'numpy.int32'>, size = 16,object = 470 (аналогичное предыдущему)

# type(i_max)= <class 'int'>, size = 14,object = 2 (i max - размер одинаков)
# type(i_max)= <class 'int'>, size = 14,object = 4

#Старый массив --- [  -9 -269  217  345  257 -481  228  346 -222 -192  111 -401  -93    4
# -168],type(array_x)= <class 'numpy.ndarray'>,size = 108 (числа от 500 до 5 миллионов ), НО при увеличении кол-ва чисел до 30
# вес увеличился с 108 до 168

# type = <class 'function'>, size = 72, object = <function change at 0x02C0F8A0
# type = <class 'int'>, size = 12, object = 0 (все переменные счетчики пока пустые)

#win 10 64

import random
import numpy as np
import sys

array_x = np.random.randint(-500000,500000,size=30)
x_min = 0
i_min = 0
x_max = 0
i_max = 0

def change(array_x,x_min,i_min,x_max,i_max):
    for i in range(0,len(array_x)-1):
        if array_x[i] > x_max:
            x_max = array_x[i]
            i_max = i
            print(f"type(x_max)= {x_max.__class__}, size = {sys.getsizeof(x_max)},object = {x_max}")
            print(f"type(i_max)= {i_max.__class__}, size = {sys.getsizeof(i_max)},object = {i_max}")
        elif array_x[i] < x_min:
            x_min = array_x[i]
            i_min = i

    print(f"Старый массив --- {array_x},type(array_x)= {array_x.__class__},size = {sys.getsizeof(array_x)}")
    print(f"Индекс наибольшего - {i_max},число {x_max}; Наименьшего - {i_min}, число {x_min}")
    array_x[i_max],array_x[i_min] = array_x[i_min],array_x[i_max]      
    print(f"Новый массив --- {array_x}")
change(array_x,x_min,i_min,x_max,i_max) 

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
show_size(change)
show_size(x_min)
show_size(i_min)
show_size(x_max)
show_size(i_max)    



# 50439 function calls (48177 primitive calls) in 4.489 seconds 
# Думаю все расписывать смысла нет, ужас творится(
#    778/39    0.002    0.000    4.204    0.108 <frozen importlib._bootstrap>:1009(_handle_fromlist)
#    217/2    0.000    0.000    4.398    2.199 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
#    149/147    0.001    0.000    1.501    0.010 <frozen importlib._bootstrap>:576(module_from_spec)
#    158/2    0.002    0.000    4.480    2.240 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
#    158/2    0.005    0.000    4.480    2.240 <frozen importlib._bootstrap>:978(_find_and_load)
#    1338    0.005    0.000    0.013    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
#    1338    0.004    0.000    0.006    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
#    462    0.001    0.000    0.001    0.000 sre_parse.py:164(__getitem__)
#    698    0.002    0.000    0.002    0.000 sre_parse.py:233(__next)
#    555    0.001    0.000    0.002    0.000 sre_parse.py:254(get)
#    312/310    0.016    0.000    0.035    0.000 {built-in method builtins.__build_class__}
#    2327    0.006    0.000    0.006    0.000 {built-in method builtins.hasattr}
#    1523/1450    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#    1664    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#    2930    0.002    0.000    0.002    0.000 {method 'rstrip' of 'str' objects}