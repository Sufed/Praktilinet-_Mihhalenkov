#Задача 6.
from math import *
a=int(input("Число 1. "))
b=int(input("Число 2. "))
c=int(input("Число 3. "))
try:
    if a or b or c<0:
        print("Число отрицательное.")
    else:
        print("Число положительное.")
        D=b**2-4*a*c
        print({D})
        if D<0:
            print("{D}>0")
except:
    print("Неправильный набор чисел.")
#Задача 4.
день=int(input("день рождения?: "))
месяц=input("месяц рождения?: ")
if месяц=='декабрь':
	знак='стрелец' if (день < 22) else 'козерог'
elif месяц=='январь':
	знак='козерог' if (день < 20) else 'водолей'
elif месяц=='февраль':
	знак='водолей' if (день < 19) else 'рыбы'
elif месяц=='март':
	знак='рыбы' if (день < 21) else 'овен'
elif месяц=='апрель':
	знак='овен' if (день < 20) else 'телец'
elif месяц=='май':
	знак='телец' if (день < 21) else 'близнецы'
elif месяц=='июнь':
	знак='близнецы' if (день < 21) else 'рак'
elif месяц=='июль':
	знак='рак' if (день < 23) else 'лев'
elif месяц=='август':
	знак='лев' if (день < 23) else 'дева'
elif месяц=='сентябоь':
	знак='дева' if (день < 23) else 'весы'
elif месяц=='октябрь':
	знак='весы' if (день < 23) else 'скорпион'
elif месяц=='ноябрь':
	знак='скорпион' if (день < 22) else 'стрелец'
print("Твой знак :",знак)
print()
print()
print()
#Задача 3.
from math import *
вопрос=input("День недели? ")
try:
    if вопрос.lower()=="да":
        number=input("Введи число от 1 до 7: ")
        if number.isdigit() and 1 <=int(number) <=7:
            дни=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
            print(f"день недели: {дни[int(number)-1]}")
        else:
            print("Viga!")
except:
    print("Ладно")
print()
print()
print()
#Задача 2.
from math import *
a=int(input("Число 1. "))
b=int(input("Число 2. "))
c=int(input("Число 3. "))
try:
    if (a,b,c)>0:
        print("Число положительное.")
        if a+b+c==180:
            if a==b and b==c:
                print("Треугольник равносторонний")
            elif a==b or a==c or b==c:
                print("Треугольник равнобедренный")
            else:
                print("Треугольник разносторонний")
    else:
        print("Число отрицательное.")
except:
    print("Неправильный набор чисел.")
print()
print()
print()
#Задача 1.
from math import *
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
