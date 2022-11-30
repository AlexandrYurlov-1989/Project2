import math
 
print("Введите числа для вычисления")
a = float(input("a = "))
b = float(input("b = "))

 
D = a + b
print(f"Сложение = {D}")
D = a - b
print(f"Вычетание = {D}")
D = a * b
print(f"Умножение = {D}")
D = a / b
print(f"Диление = {D}")
D = a ** b
print(f"Возведение числа a в степень b = {D}")
D = a % b
print(f"Деления числа a по модулю b = {D}")
D = a // b
print(f"Целочисленное деления числа a на b = {D}")