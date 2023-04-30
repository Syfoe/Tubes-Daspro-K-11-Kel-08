from fungsi import *
# login
login = False
def log_in():
    global login
    if login:
        print("Login gagal!")
    else:
        user = input()
        password = input()

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

        print(database)

        for i in range(panjangData):
            for j in range(3):
                if (j == 0):
                    users[i] = database[i][j]
                elif (j == 1):
                    passwords[i] = database[i][j]

        file.close()
        user_match = False
        password_match = False
        for i in range(len_arr(users)):
            if(user == users[i]):
                user_match = True

        for i in range(len_arr(passwords)):
            if (password == passwords[i]):
                password_match = True

        if (user_match):
            if (password_match):
                print("selamat datang, " + str(user) + '!')
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil')
            else:
                print("Password salah!")
        else:
            print("Username tidak terdaftar!")

        login = True

log_in()