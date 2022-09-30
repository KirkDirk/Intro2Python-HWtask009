# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

tempnum = num = int(input('Введите число N: '))
numlist = []
for i in range(tempnum*2+1):
    numlist.append(i-tempnum)
print(numlist)

with open('C:\Sas\LearningGB\Intro2Python\HW\HWtask009/data.txt', 'r') as data:
    xnum = (data.readline()).split()
    print(xnum)
data.close

numresult = 1
for i in range(len(xnum)):
    numresult *= numlist[int(xnum[i])]
print(numresult)