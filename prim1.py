n = input("Введите трехзначное целое число:")
x = 1
y = 0
for i in n:
	y += int(i)
	if int(i) != 0:
		x *= int(i)
 
print("Сумма цифр:", y)
print("Произведение цифр:", x)