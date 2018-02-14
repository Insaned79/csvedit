from pandas import read_csv
import os

print('Введите имя файла [test.csv]')
filename=str(input())

if filename=='':
    filename='test.csv'

if not os.path.exists(filename):
    print('Файл не найден')
    quit(2)
csv = read_csv('test.csv', sep=',', header=0, low_memory=False)
sz=str(len(csv))
print('Загружено строк: '+sz)
print('Первые пять: ')
print(csv[:5])





