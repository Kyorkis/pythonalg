#Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

chislo = input("Введите число:")
if chislo.isdigit():

    reverse = chislo[::-1]
    print(f'Перевернутое число: {reverse}')

elif chislo.isdigit() == False:
    print("Вы ввели не число!!!")