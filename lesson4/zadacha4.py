#Определить, какое число в массиве встречается чаще всего

#  50419 function calls (48157 primitive calls) in 0.689 seconds 
#  100 loops, best of 5: 41 nsec per loop

import random
import numpy as np
import cProfile

array_x = np.random.randint(-10,10,size=30)
print(array_x)

max_count = 0
char = array_x[0]

for i in range(0,len(array_x)-1):
    count = 1
    for q in range(i+1,len(array_x)):
        if array_x[i]==array_x[q]:
            count +=1
    if count >max_count:
        max_count = count
        char = array_x[i]
print(f"{max_count} раз(a), встречается число : {char}")      










