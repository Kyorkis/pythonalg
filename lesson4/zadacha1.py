# Написать два алгоритма нахождения i-го по счёту простого числа.
#  Первый - использовать алгоритм решето Эратосфена. 
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

# 100 loops, best of 5: 41 nsec per loop (n=50)
# 100 loops, best of 5: 41 nsec per loop (n=30)

# 627 function calls (620 primitive calls) in 0.006 seconds (n=30)
# 632 function calls (625 primitive calls) in 0.006 seconds (n = 50)
# 652 function calls (645 primitive calls) in 0.013 seconds (n = 150)
# 856 function calls (849 primitive calls) in 0.456 seconds (n=1500)
# 1047 function calls (1040 primitive calls) in 1.969 seconds(n=3000)

import timeit
import cProfile

n = 3000 

lst = []
k = 0
for i in range(2,n+1):
    for j in range(2,i):
        if i %j == 0:
            k = k+1
    if k ==0:
        lst.append(i)
    else:
        k = 0
print (lst)     

#print(timeit.timeit(lst))


