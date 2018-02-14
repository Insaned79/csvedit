from pandas import read_csv

csv = read_csv('test.csv', sep=',', header=0, low_memory=False)

min = -1
max = -1

s= csv.iloc[100]
print (str(s))

