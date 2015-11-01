#coding: utf-8

import pickle
import os
"""
easyInt = 13

pickle.dump(easyInt,open("myNewFileForTestPickleDump.txt","wb"),protocol=3)

dePickleResult = pickle.load(open("myNewFileForTestPickleDump.txt","rb"))

print (dePickleResult)
"""

continueFlag = True

listOfCar = [] 
if os.path.exists("FileWithListOfCar.txt"):
    listOfCar = pickle.load(open("FileWithListOfCar.txt","rb")) #Считывание с файла

while continueFlag:
    #Предложить пользователю выбрать одно из возможных действий
    userChange = input("Что делать:\n 1.Добавить новый автомобиль?\n"
                       " 2.Вывести все автомобили?\n 3.Вывести автомобили по условию?\n")

    if userChange == "1":
        #Происходит добавление нового автомобиля в файл
        inputStrCarName = input("Введите имя автомобиля:")
        inputStrCarPower = input("Введите мощность автомобиля:")

        if inputStrCarPower.isdigit():
            listOfCar.append(inputStrCarName + " " + inputStrCarPower)
        else:
            print("Ошибка ввода!\n")

    elif userChange == "2":
        #Вывод списка всех автомобилей, которые входят в файл
        listOfCar.sort()
        print(listOfCar)

    elif userChange == "3":
        #Надо сделать ещё один выбор для пользователя, какое будет условие фильтрации
        userChangeFilter = input("Как сортировать:\n 1.По мощности?\n"
                       " 2.По вхождению слова в название?\n 3.По полному соответствию слова?\n")
        
        if userChangeFilter == "1":
        #Здесь сортируем по мощности и приводим третий выбор как именно
            userChangePower = input("Как фильтровать:\n 1.Конкретное число?\n"
                           " 2.Больше?\n 3.Меньше?\n 4.В промежутке?\n")
            
            if userChangePower == "1":
            #При вводе конкретного числа
                dreamPower = input("Введите желаему мощность\n")
                for car in listOfCar:
                    carPower = int(car[car.find(' '):])
                    if carPower == int(dreamPower):
                        print(car)
                    
            elif userChangePower == "2":
            #при вводе числа больше заданного
                dreamPower = input("Введите желаему мощность\n")
                for car in listOfCar:
                    carPower = int(car[car.find(' '):])
                    if carPower > int(dreamPower):
                        print(car)
                    
            elif userChangePower == "3":
            #при вводе числа меньше заданного
                dreamPower = input("Введите желаему мощность\n")
                for car in listOfCar:
                    carPower = int(car[car.find(' '):])
                    if carPower < int(dreamPower):
                        print(car)
                    
            elif userChangePower == "4":
            #При вводе желаемого промежутка 
                dreamPowerMax = input("Введите максимальную мощность:\n")
                dreamPowerMin = input("Введите минимальную мощность:\n")
                for car in listOfCar:
                    carPower = int(car[car.find(' '):])
                    if carPower >= int(dreamPowerMin) and carPower <= int(dreamPowerMax):
                        print(car)
                    
                    
        elif userChangeFilter == "2":
        #Производим поиск по вхождению слова в название
            wordName = input("Введите слово: \n")
            for car in listOfCar:
                carName = car[:car.find(' ')]
                if carName.find(wordName) > -1:
                    print(car)
                
                
        elif userChangeFilter == "3":
        #Производим поиск автомобиля по полному соответствию слова
            wordName = input("Введите слово: \n")
            for car in listOfCar:
                carName = car[:car.find(' ')]
                if carName == wordName:
                    print(car)

    if input("Продолжить работу? да(1)/нет(0)?\n") == "1":
        continue
    else:
        continueFlag = False

pickle.dump(listOfCar,open("FileWithListOfCar.txt","wb"),protocol=3)
