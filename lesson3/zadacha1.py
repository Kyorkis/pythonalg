#В диапазоне натуральных чисел от 2 до 99 определить,
#сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# type = <class 'int'>, size = 14, object = 8
# type = <class 'int'>, size = 14, object = 9
# type = <class 'list'>, size = 68, object = [4, 3, 2, 1, 1, 1, 1, 1]
#Win 10 64

import cProfile
import sys

x = [0]*8
def diap(x):
    for i in range(2,10):
        for j in range(2,10):
            return(f"{i}:{j}")
        if i%j==0:
            x[j-2] +=1

    i = 0
    while i<len(x):
        return(f"{i+2}-{x[i]}")
    i+=1
print(diap(x))                        
#for i in range(2,10):
#    for j in range(2,10):
#        print(f"{i}:{j}")
#        if i%j==0:
#            x[j-2] += 1
            
#i=0
#while i<len(x):
#    print(f'{i+2}-{x[i]}')
#    i+=1
#x = [0]*8
#ef diap():
#    for i in range(2,10):
#        for j in range(2,10):
#            if i%j==0:
#                x[j-2] +=1

#    i=0
#    while i<len(x):
#        p = (f"{i+2}-{x[i]}")
#        return p
#        i+=1
#z = diap()
#print(z)   



#def show_size(x, level=0):
#    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

#    if hasattr(x, '__iter__'):
#        if hasattr(x, 'items'):
#            for y in x.items():
#                show_size(y, level + 1)

#        elif not isinstance(x, str):
#            for y in x:
#                show_size(y, level + 1)


#show_size(i)
#show_size(j)
#show_size(x)                


