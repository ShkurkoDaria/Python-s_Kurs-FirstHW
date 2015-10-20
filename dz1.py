#coding: utf-8
# Это часть ДЗ с занятия в классе
import math

f = open("textFile.txt",'r')

str = f.read()

#print(str)

list = str.split()

for element in list:
    print(element)

one = float(list[0]) + float(list[1])

print(one)

two = math.sqrt(float(list[2])*float(list[3]))

print(two)

list1 = []

#list.append(one)
list1.append(two)
list1.append(one)
list1.sort(reverse=True)

three = list1[0]

#print("Это такая то штука" + three)

print(three)


four = math.cos(float(list[4]))

print(four)

f.close()

# Это уже нормальная часть ДЗ

# --------------Part 1------------------------------------------

import os
import math

D1 = 45 # Диаметр 1 круга
D2 = 338 # Диаметр 2 круга
D3 = 19 # Диаметр 3 круга

# расчет площадей
S1 = math.pi*pow(D1,2)/4
S2 = math.pi*pow(D2,2)/4
S3 = math.pi*pow(D3,2)/4

# Вывод площадей на экран
print(S1, S2, S3)

# Из третьей площади круга вычесть площадь двух других кругов и вывод итога на экран
itog = S3 - (S1 + S2)
в
print(itog)

#---------------Part 2------------------------------------------

A = [1, -20, 38, 0, 44]
B = [88, -20, 48, 4, 33,2]

for i in range(len(A)):
    if A[i] < B[i]:
        print(A[i])
    else:
        print(B[i])

        
    if abs(A[i] - B[i]) < 15:
        print('Congratulations!')
    else:
        print('Sorry, but your summ > 15!')
        
#---------------Part 3------------------------------------------
a = input("a = ")
b = input("b = ")
c = input(" +/- ") # Выбор действия сложения или вычитания

if c == '+':
    print ("Summ a, b = " + str(int(a)+int(b)))
elif c == '-':
    print ("Difference a, b = " + str(int(a)-int(b)))
else:
    print ("Error")
