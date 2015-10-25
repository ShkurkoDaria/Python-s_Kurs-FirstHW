#coding:utf-8

s = ['Виталий Жуков', 'Дарья Шкурко', 'Дмитрий Синицкий',
     'Игорь Лавров', 'Андрей Ульянов', 'Павел Щербаков',
     'Игорь Друзь', 'Дмитрий Гусь']

# Вывод имени одного студента на экран

index = int(input("Введите индекс студента: "))
print("Под индексом", index, s[index-1][:s[index-1].find(' ')])

#Вывод имен нескольких студентов

start = int(input("\nВведите начальный индекс: "))
finish = int(input("Введите конечный индекс: "))
print("Срез s[", start, ":", finish, "] - это", end=" ")
s1 = s[start-1:finish]

for ind in range(len(s1)):
    s1[ind] = s1[ind][:s1[ind].find(' ')]
print(s1)

#Находим имена студентов в именах которых есть буква "р"

number = 0
for fi in s:
    fi = fi[:fi.find(' ')]
    if fi.find('р') >= 0:
        number += 1
print('\nКоличество людей с буквой "р" в имени = ', number)

#Находим группы студентов с одинаковыми именами и создаем списки тих групп

groups = []

for ind in range(len(s)):
    nezachem = False

    if(len(groups) != 0):
        for sp in groups:
            if(len(sp) != 0):
                if(sp[0][:sp[0].find(' ')] == s[ind]):
                    nezachem = True
                    break

    if(nezachem != True):
        spisok = []

        for ind1 in range(len(s)-ind - 1):
            if s[ind][:s[ind].find(' ')] == s[ind1+ind+1][:s[ind1+ind+1].find(' ')]:
                if(len(spisok) != 0):
                    spisok.append(s[ind1+ind+1])
                else:
                    spisok.append(s[ind])
                    spisok.append(s[ind1+ind+1])

        if(len(spisok) != 0):
            groups.append(spisok)
    else:
        continue

print("\nСтуденты с одинаковыми именами: ", groups)
