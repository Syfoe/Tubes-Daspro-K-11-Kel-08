import random
from fungsi import *
"""bahan = random.randint(0,5)
print(bahan)

file = open('bahan_bangunan.csv', 'r')
b = file.readlines()
print(b)
data_bahan = ['' for i in range(len_arr(b)-1)]
print(data_bahan)
for i in range(-1,-len_arr(data_bahan) - 1,-1):
    data_bahan[i] = b[i]

for i in range (len_arr(data_bahan)):
    data_bahan[i] = strip(data_bahan[i],'\n')
    data_bahan[i] = split(data_bahan[i],';')
file.close()
print(data_bahan)


file = open("candi.csv", 'r')
c = file.readlines()
panjang_data_candi = len_arr(c) - 1 
data_candi = ['' for i in range(panjang_data_candi)]
for i in range(-1,-panjang_data_candi - 1, -1):
    data_candi[i] = c[i]

for i in range(panjang_data_candi):
    data_candi[i] = strip(data_candi[i],'\n')
    data_candi[i] = split(data_candi[i],';')
file.close()
"""
x = int(input("angka: "))
a =[["a", '12'], ['b', '12']]
b = int(a[0][1])
if(x < b):
    print(1)
else:
    print(2)
