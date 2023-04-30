from fungsi import *
file = open("user.csv", 'r')
a = file.readlines()
panjangData = len_arr(a) - 1
database = ['' for i in range(panjangData)]

for i in range(-1,-len_arr(a)-1,-1):
    if (i != -len_arr(a)):
        database[i] = a[i]

for i in range(panjangData):
    database[i] = strip(database[i],'\n')
    database[i] = split(database[i],';')

users = ['' for i in range(panjangData)]
passwords = ['' for i in range(panjangData)]

for i in range(panjangData):
    for j in range(3):
        if (j == 0):
            users[i] = database[i][j]
        elif (j == 1):
            passwords[i] = database[i][j]
file.close()
print(users)
print(passwords)