#coding: utf-8

import pickle
import os

def inputListFromFilePickle(fileName):
    list = []
    if os.path.exists(fileName):
        list =  pickle.load(open(fileName,"rb")) #Считывание с файла
    return list

def outputListToFilePickle(listOfCar, fileName):
    pickle.dump(listOfCar,open(fileName,"wb"),protocol=3)
    return 0

def inputCommand():
    command = ""
    #Предложить пользователю выбрать одно из возможных действий
    userChange = input("Что делать:\n 1.Добавить новый автомобиль?\n"
                       " 2.Вывести все автомобили?\n 3.Вывести автомобили по условию?\n")
                       
    if userChange == "1":
        command += userChange
    elif userChange == "2":
        command += userChange
    elif userChange == "3":
        command += userChange
        #Надо сделать ещё один выбор для пользователя, какое будет условие фильтрации
        userChangeFilter = input("Как сортировать:\n 1.По мощности?\n"
                       " 2.По вхождению слова в название?\n 3.По полному соответствию слова?\n")

        if userChangeFilter == "1":
        #Здесь сортируем по мощности и приводим третий выбор как именно
            command += userChangeFilter
            userChangePower = input("Как фильтровать:\n 1.Конкретное число?\n"
                           " 2.Больше?\n 3.Меньше?\n 4.В промежутке?\n")

            if userChangePower == "1":
                command += userChangePower
            elif userChangePower == "2":
                command += userChangePower
            elif userChangePower == "3":
                command += userChangePower
            elif userChangePower == "4":
                command += userChangePower

        elif userChangeFilter == "2":
            command += userChangeFilter
        elif userChangeFilter == "3":
            command += userChangeFilter
    return command

continueFlag = True

listOfCar = []
listOfCar = inputListFromFilePickle("FileWithListOfCar.txt")

while continueFlag:
    myCommand = inputCommand()

    if myCommand[0] == "1":
        #Происходит добавление нового автомобиля в файл
        inputStrCarName = input("Введите имя автомобиля:")
        inputStrCarPower = input("Введите мощность автомобиля:")

        if inputStrCarPower.isdigit():
            listOfCar.append(inputStrCarName + " " + inputStrCarPower)
        else:
            print("Ошибка ввода!\n")

    elif myCommand[0] == "2":
        #Вывод списка всех автомобилей, которые входят в файл
        listOfCar.sort()
        print(listOfCar)

    elif myCommand[0] == "3":
        if myCommand[1] == "1":
            if myCommand[2] == "1":
            #При вводе конкретного числа
                dreamPower = input("Введите желаему мощность\n")
                for car in listOfCar:
                    carPower = int(car[car.find(' '):])
                    if carPower == int(dreamPower):
                        print(car)

            elif myCommand[2] == "2":
            #при вводе числа больше заданного
                dreamPower = input("Введите желаему мощность\n")
                for car in listOfCar:
                    carPower = int(car[car.find(' '):])
                    if carPower > int(dreamPower):
                        print(car)

            elif myCommand[2] == "3":
            #при вводе числа меньше заданного
                dreamPower = input("Введите желаему мощность\n")
                for car in listOfCar:
                    carPower = int(car[car.find(' '):])
                    if carPower < int(dreamPower):
                        print(car)

            elif myCommand[2] == "4":
            #При вводе желаемого промежутка
                dreamPowerMax = input("Введите максимальную мощность:\n")
                dreamPowerMin = input("Введите минимальную мощность:\n")
                for car in listOfCar:
                    carPower = int(car[car.find(' '):])
                    if carPower >= int(dreamPowerMin) and carPower <= int(dreamPowerMax):
                        print(car)


        elif myCommand[1] == "2":
        #Производим поиск по вхождению слова в название
            wordName = input("Введите слово: \n")
            for car in listOfCar:
                carName = car[:car.find(' ')]
                if carName.find(wordName) > -1:
                    print(car)


        elif myCommand[1] == "3":
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

outputListToFilePickle(listOfCar, "FileWithListOfCar.txt")
