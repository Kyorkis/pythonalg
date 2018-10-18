#Написать программу, которая генерирует в указанных пользователем границах:
#случайное целое число;
#случайное вещественное число;
#случайный символ. Для каждого из трех случаев пользователь задает свои 
# границы диапазона. Например, если надо получить случайный символ от 'a' до 'f',
#  то вводятся эти символы. Программа должна вывести на экран любой символ 
# алфавита от 'a' до 'f' включительно.


import random 
import string
x = str(input("Введите первую букву или цифру: "))
y = str(input("Введите вторую букву или цифру: "))
if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)
    if x>y:
        print("Случайное число: ",random.randint(y,x))  
    else:
        print("Случайное число: ",random.randint(x,y))
elif x.isdigit() or y.isdigit() != False:
    print("Вы ввели цифру и букву одновременно")                
else:
    x = x.lower()
    y = y.lower()
    ctroka = string.ascii_lowercase
    zx = ctroka.index(x)
    zy = ctroka.index(y) 
    if zx > zy:
        srez = random.choice(ctroka[zy:zx])
        print("Случайная буква:",srez)
    else:
        srez = random.choice(ctroka[zx:zy])
        print("Случайная буква:",srez)     
