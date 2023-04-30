from fungsi import *
login = False

# matriks data (username, password, role)
file = open("user.csv", 'r')
a = file.readlines()
panjangData = len_arr(a) - 1
database = ['' for i in range(panjangData)]

## loop untuk filter data
for i in range (-1,-panjangData-1,-1):
    database[i] = a[i]

for i in range(panjangData):
    database[i] = strip(database[i],'\n')
    database[i] = split(database[i],';')
file.close()
print(database)
role = ''
username = ''


# F01 fungsi login
def F01():
    global login
    global role
    global username
    if login:
        print("Login gagal!")
        print(f'And telah login dengan username {username}, silahkan lakukan "logout" sebelum melakukan login kembali.')
    else:
        user = input("usename: ")
        password = input("password: ")

        user_match = False
        password_match = False

        for i in range(len_arr(database)):
            if (user == database[i][0]):
                user_match = True
            if (password == database[i][1]):
                password_match = True
            if (password_match and user_match):
                indeksPlayer = i
                break
    

        if (user_match):
            if (password_match):
                print("selamat datang, " + str(user) + '!')
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil')
                login = True
                role = database[indeksPlayer][2]
                username = database[indeksPlayer][0]
                print("role: ", role)
                print('username', username)
            else:
                print("Password salah!")
        else:
            print("Username tidak terdaftar!")

        

# F02 fungsi logout
def F02():
    global login
    if login:
        login = False
        print("logout berhasil")
    else:
        print("logout gagal")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        
# F05
def F05 ():
    global role
    if(role == "bandung_bondowoso"):
    
        username_jin = input("Masukkan username jin: ")
        a = False
        for i in range (len_arr(database)):
            if username_jin == database[i][0]:
                a = True
                indeksUser = i
                break
                
        if a == False:
            print("Tidak ada jin dengan username tersebut.")
        else:
                if database[indeksUser][2] == "pengumpul":
                    konfirmasi = input(f"Jin ini bertipe \"{database[indeksUser][2]}\". Yakin ingin mengubah ke tipe \"Pembangun\"(Y/N)?")
                    if konfirmasi == "Y":
                        print("Jin telah berhasil diubah.")
                        database[indeksUser][2] = "pembangun"
                else:
                    konfirmasi = input(f"Jin ini bertipe \"{database[indeksUser][2]}\". Yakin ingin mengubah ke tipe \"Pengumpul\"(Y/N)?")
                    if konfirmasi == "Y":
                        print("Jin telah berhasil diubah.")
                        database[indeksUser][2] = "pengumpul"
    else:
        print("maaf anda bukan bandung bondowoso. Akses ditolak")

while True:
    pilihan = input(">>> ")
    if (pilihan == 'login'):
        F01()
    elif (pilihan == 'logout'):
        F02()
    elif (pilihan == 'ubahjin'):
        F05()
    elif (pilihan == 'exit'):
        break
