# Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.


import random 
import string
x = input("Введите первую букву английского алфавита:")
y = input("Введите вторую букву английского алфавита:")
z = string.ascii_lowercase
x = x.lower()
y = y.lower()
x1= z.index(x)
y1= z.index(y)
if x1 > y1:
    rast=x1-y1
    print("Индекс первой буквы - {}, второй - {}, расстояние между ними {}".format(x1,y1,rast))
else:
    rast=y1-x1
    print("Индекс первой буквы - {}, второй - {}, расстояние между ними {}".format(x1,y1,rast))
print(z.index(x))    