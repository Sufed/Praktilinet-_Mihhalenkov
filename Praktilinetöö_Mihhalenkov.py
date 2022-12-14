#Задача 2.
from math import *
a=int(input("Число 1. "))
b=int(input("Число 2. "))
c=int(input("Число 3. "))
try:
    if (a,b,c)>0:
        print("Число положительное.")
        if a+b+c==180:
            if a==b==c:
                print("Треугольник равносторонний")
    else:
        print("Число отрицательное.")
except:
    print("Неправильный набор чисел.")









































print()
print()
print()
#Задача 1.
number=float(input("Введите число: "))
try:
    if number>0:
        print("Число положительное.")
    else:
        print("Число отрицательное.")
except:
    print("Неправильный набор чисел.")
try:
    if number%2==1:
        print("Число нечетное.")
    else:
        print("Число четное.")
except:
    print("Неправильный набор чисел.")