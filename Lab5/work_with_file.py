import csv
import sys
print(' First group: ')
print("")
#ЗАПИС ДАННИХ
fd1=open("first_group.txt", 'w', encoding= 'utf-8')
fd1.write('Катя, 55\nВова, 60\nОля, 82\nКирило, 49\nСаша, 66\nМикола, 91\n')
fd1.close()

#ДОЗАПИС ДАННИХ
fd1 = open('first_group.txt', 'a', encoding='utf-8 \n')
fd1.write('Софія, 81 \n')
fd1.write('Данило, 40 \n')
fd1.write('Михайло, 89 \n')
fd1.close()

#ЧИТАННЯ ФАЙЛУ
print('\n')
fd1=open("first_group.txt", encoding= 'utf-8')#відкриття файлів
reader = csv.reader(fd1,delimiter="\t")#читання інформації
for row in reader:
    print(row)
fd1.close()

print("")
print(' Second group: ')
print("")
#ЗАПИС ДАННИХ
fd2=open("second_group.txt",'w', encoding= 'utf-8')
fd2.write('Марія, 88\nМикола, 67\nОлексій,54\nАнтоніна, 75\nОлег, 48\nМаксим, 62\nДмитро, 66\nТетяна, 78\nПетро, 69\n')
fd2.close()
    
#ДОЗАПИС ДАННИХ
fd2 = open('second_group.txt', 'a', encoding='utf-8\n')
fd2.write('Степан, 61 \n')
fd2.write('Наталія, 85 \n')
fd2.close()

#ЧИТАННЯ ФАЙЛУ
fd2=open("second_group.txt", encoding= 'utf-8')
reader = csv.reader(fd2,delimiter="\t")
for row in reader:
    print(row)
###   ПОШУК ДАННИХ У ФАЙЛІ   ###
import io
print("Пошук данних у файлі")
print('')
print("Введіть слово або символ, який шукаєте:")
word = input()
print("Введіть назву файлу:")
filename = input()
with io.open(filename, encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, end='')
file.close()
print("")
###   ПОШУК ФАЙЛІВ У КАТАЛОЗІ   ###

print('Пошук файлів у каталозі:')
print('')
import glob
for filename in glob.glob("*.txt"):
        print(filename)
print('')    
print('')
###   СОРТУВАННЯ ДАННИХ ЗА СЕРЕДНІМ БАЛОМ ###
print("ГРУПА №1:")
f1 = open("first_group.txt", encoding = 'utf-8')
D1 = {}
for lines in f1:
        strings = lines.split(',')
        key = strings[0].rstrip()
        value = int(strings[1])
        D1[key] = value

for i in sorted(D1.items(),key=lambda para: (para[1],para[0])):
        print(i)
f1.close()

print('\n')
print("ГРУПА №2:")
f2 = open("second_group.txt", encoding = 'utf-8')
D2 = {}
for lines in f2:
        strings = lines.split(',')
        key = strings[0].rstrip()
        value = int(strings[1])
        D2[key] = value

for i in sorted(D2.items(),key=lambda para: (para[1],para[0])):
        print(i)
f2.close()


