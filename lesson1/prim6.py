#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


import string
x = int(input("Введите номер буквы:"))
alf = string.ascii_lowercase
letter= alf[x]
print("Ваша буква:",letter)