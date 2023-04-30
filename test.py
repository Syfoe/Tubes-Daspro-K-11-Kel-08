from fungsi import *
file = open("user.csv", 'r')
a = file.readlines()
panjangData = len_arr(a) - 1
database = ['' for i in range(panjangData)]

for i in range(-1,-panjangData - 1,-1):
    database[i] = a[i]

