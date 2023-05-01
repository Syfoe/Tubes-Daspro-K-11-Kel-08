from fungsi import *
import random
login = False

#fungsi update file
def update(namaFile: str, matriks: list[list[str]]):
    with open(namaFile, 'w', encoding='utf-8') as file:
        if (namaFile == "user.csv"):
            file.write("username;password;role\n")
            for i in range(len_arr(matriks)):
                for j in range(3):
                    if(i != len_arr(matriks) -1):
                        if(j == 2):
                            file.write(matriks[i][j])
                            file.write("\n")
                        else:
                            file.write(matriks[i][j])
                            file.write(";")
                    else:
                        if(j == 2):
                            file.write(matriks[i][j])
                        else:
                            file.write(matriks[i][j])
                            file.write(";")
        elif (namaFile == 'bahan_bangunan.csv'):
            file.write("nama;deskripsi;jumlah\n")
            for i in range(len_arr(matriks)):
                for j in range(3):
                    if(i != len_arr(matriks) - 1):
                        if(j == 2):
                            file.write(str(matriks[i][j]))
                            file.write("\n")
                        else:
                            file.write(str(matriks[i][j]))
                            file.write(";")
                    else:
                        if(j == 2):
                            file.write(str(matriks[i][j]))
                        else:
                            file.write(str(matriks[i][j]))
                            file.write(';')
        elif (namaFile == 'candi.csv'):
            file.write ('id;pembuat;pasir;batu;air\n')
            for i in range(len_arr(matriks)):
                for j in range(5):
                    if(i != len_arr(matriks)-1):
                        if(j == 4):
                            file.write(str(matriks[i][j]))
                            file.write('\n')
                        else:
                            file.write(str(matriks[i][j]))
                            file.write(';')
                    else:
                        if(j == 4):
                            file.write(str(matriks[i][j]))
                        else:
                            file.write(str(matriks[i][j]))
                            file.write(';')
                            

        

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

# matriks untuk dadta bahan bangunan
file = open('bahan_bangunan.csv', 'r')
b = file.readlines()
data_bahan = ['' for i in range(len_arr(b)-1)]
for i in range(-1,-len_arr(data_bahan) - 1,-1):
    data_bahan[i] = b[i]

for i in range (len_arr(data_bahan)):
    data_bahan[i] = strip(data_bahan[i],'\n')
    data_bahan[i] = split(data_bahan[i],';')
file.close()
print(data_bahan)


#matriks data candi
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


candi_built = len_arr(data_candi)
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
        user = input("username: ")
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
    global username
    global role
    if login:
        login = False
        username = ''
        role = ''
        print('"logout" berhasil')
    else:
        print('"logout" gagal')
        print('Anda belum "login", silahkan "login" terlebih dahulu sebelum melakukan "logout"')

# F03
def F03():
    global database
    global role
    global login
    if login:
        if (role == 'bandung_bondowoso'):
            if (len_arr(database) < 100):
                print("""
Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi
                """)
                jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
                while(jenis_jin != 1 and jenis_jin != 2):
                    print(f'Tidak ada jenis jin bernomor "{jenis_jin}"')
                    jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
                if (jenis_jin == 1):
                    print('Memilih jin "Pengumpul".')
                elif (jenis_jin == 2):
                    print('Memilih jin "Pembangun".')
                nama_jin = input("Masukkan username jin: ")
                nama_found = False
                pass_found = False
                for i in range(len_arr(database)):
                    if (database[i][0] == nama_jin):
                        nama_found = True

                while (nama_found):
                    nama_found = False
                    print("username jin sudah diambil")
                    nama_jin = input("Masukkan username jin: ")
                    for i in range(len_arr(database)):
                        if(database[i][0] == nama_jin):
                            nama_found = True

                pass_jin = input("Masukkan password jin: ")
                if(len(pass_jin) < 5 or len(pass_jin) >25):
                    pass_found = True

                while (pass_found):
                    pass_found = False
                    print("Password panjangnya harus 5-25 karakter!")
                    pass_jin = input("Masukkan password jin: ")
                    if(len(pass_jin) < 5 or len(pass_jin) >25):
                        pass_found = True
                
                print("""
Mengumpulkan sesajen...
Menyerahkan sesajen...
Membacakan mantra...
                """)
                print(f'Jin {nama_jin} berhasil dipanggil!')
                jinbaru = ['','','']
                for i in range (3):
                    if (i == 0):
                        jinbaru[i] = nama_jin
                    elif (i == 1):
                        jinbaru[i] = pass_jin
                    else:
                        if(jenis_jin == 1):
                            jinbaru[i] = "jin_pengumpul"
                        else:
                            jinbaru[i] = "jin_pembangun"
                database = konso(database,jinbaru)
                update("user.csv",database)
            else:
                print("penuh")
        else:
            print("anda bukan bondowoso. Akses ditolak")
    else:
        print('Anda belum login. Harap login terlebih dahulu!')
        F15()    

# F04
def F04():
    global database
    global login
    global role
    if login:
        if (role == 'bandung_bondowoso'):
            nama_jin = input("Masukkan username jin: ")
            name_found = False
            data_jin = ""
            for i in range (len_arr(database)):
                if (database[i][0] == nama_jin):
                    name_found = True
                    data_jin = database[i]

            if (name_found):
                choice = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ")
                if (choice == 'Y' or choice == "y"):
                    database = delete_elemen(database,data_jin)
                    update('user.csv', database)
                    print("Jin berhasil dihapus dari alam gaib")
                elif (choice == 'N' or choice == 'n'):
                    print("Jin tidak berhasil dihapus dari alam gaib")
                else:
                    print("input salah")
            else:
                print("Tidak ada jin dengan username tersebut.")
        else:
            print('Anda bukan Bandung Bondowoso. Akses ditolak')
    else:
        print('Anda belum login. Harap login terlebih dahulu!')
        F15()

# F05
def F05 ():
    global role
    global database
    global login
    if login:
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
                    if database[indeksUser][2] == "jin_pengumpul":
                        konfirmasi = input(f"Jin ini bertipe \"{database[indeksUser][2]}\". Yakin ingin mengubah ke tipe \"Pembangun\"(Y/N)?")
                        if (konfirmasi == "Y" or konfirmasi == "y"):
                            print("Jin telah berhasil diubah.")
                            database[indeksUser][2] = "jin_pembangun"
                            print(database)
                            update('user.csv', database)
                    else:
                        konfirmasi = input(f"Jin ini bertipe \"{database[indeksUser][2]}\". Yakin ingin mengubah ke tipe \"Pengumpul\"(Y/N)?")
                        if (konfirmasi == "Y" or konfirmasi == 'y'):
                            print("Jin telah berhasil diubah.")
                            database[indeksUser][2] = "jin_pengumpul"
                            print(database)
                            update("user.csv", database)
        else:
            print("maaf anda bukan bandung bondowoso. Akses ditolak")
    else:
        print('Anda belum login. Harap login terlebih dahulu!')
        F15()

# F06
def F06():
    global role
    global login
    global data_bahan
    global data_candi
    global candi_built
    global username
    if login:
        if (role == 'jin_pembangun'):
            need_air = random.randint(0,5)
            need_batu = random.randint(0,5)
            need_pasir = random.randint(0,5)
            cukup = True
            if ((need_air > int(data_bahan[0][2])) or (need_batu > int(data_bahan[1][2])) or (need_pasir > int(data_bahan[2][2]))):
                cukup = False
            if(cukup):
                data_bahan[0][2] = int(data_bahan [0][2]) - need_air
                data_bahan[1][2] = int(data_bahan [1][2]) - need_batu
                data_bahan[2][2] = int(data_bahan [2][2]) - need_pasir
                update('bahan_bangunan.csv', data_bahan)
                print("Candi berhasil dibangun.")
                data_candi_baru = [str(candi_built + 1), username, str(need_pasir), str(need_batu), str(need_air)]
                data_candi = konso(data_candi,data_candi_baru)
                update('candi.csv', data_candi)
                candi_built += 1
                print(f'sisa candi yang perlu dibangun: {100-candi_built}')
            else:
                print("Bahan bangunan tidak mencukupi.")
                print("Candi tidak bisa dibangun!")
        else:
            print("Anda bukan Jin Pembangun. Akses ditolak")
    else:
        print('Anda belum login. Harap login terlebih dahulu!')
        F15()

# F07
def F07():
    global role
    global data_bahan
    global username
    global login
    if login:
        if(role == 'jin_pengumpul'):
            collect_air = random.randint(0,5)
            collect_batu = random.randint(0,5)
            collect_pasir = random.randint(0,5)
            print(f'Jin {username} menemukan {collect_pasir} pasir, {collect_batu} batu, {collect_air} air')
            data_bahan[0][2] = str(int(data_bahan[0][2]) + collect_air)
            data_bahan[1][2] = str(int(data_bahan[1][2]) + collect_batu)
            data_bahan[2][2] = str(int(data_bahan[2][2]) + collect_pasir)
            update('bahan_bangunan.csv', data_bahan)
        else:
            print("Anda bukan Jin Pengumpul. Akses ditolak")
    else:
        print('Anda belum login. Harap login terlebih dahulu!')
        F15()


# F12 ayamberkokok
def F12(user, batchbangun):
    if user == "roro_jonggrang": 
        jumlah_candi = batchbangun
        print("Kukuruyuk.. Kukuruyuk..")
        print()
        if jumlah_candi == 100: 
            print("Jumlah Candi: " + str(jumlah_candi))
            print()
            print("Yah, Bandung Bondowoso memenangkan permainan!")
        else:
            print("Jumlah Candi: " + str(jumlah_candi))
            print()
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print()
            print("*Bandung Bondowoso angry noise*")
            print()
            print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("Maaf anda tidak memiliki akses, command ini hanya dapat digunakan oleh Roro Jonggrang")

# F15
def F15():
    global role
    if (role == ''):
        print("""
=========== HELP ===========
1. login
Untuk masuk menggunakan akun
2. exit
Untuk keluar dari program dan kembali ke terminal
              """)
    elif (role == 'bandung_bondowoso'):
        print("""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan
2. summonjin
   Untuk memanggil jin
3. hapusjin
   Untuk menghilangkan jin
4. ubahjin
   Untuk mengubah tipe jin
5. batchkumpul
   Untuk mengerahkan jin untuk mengumpulkan bahan bangunan
6. batchbangun
   Untuk mengerahkan jin untuk membangun candi
7. laporanjin
   Untuk mengetahui kinerja seluruh jin
8. laporancandi
   Untuk mengetahui progress pembangunan candi
9. save
   Untuk menyimpan data permainan
10. exit
   Untuk keluar dari program
        """)
    elif(role == 'roro_jonggrang'):
        print("""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan
2. hancurkancandi
   Untuk menghancurkan candi yang tersedia
3. ayamberkokok
   Untuk menyelesaikan permainan
4. save
   Untuk menyimpan data permainan
5. exit
   Untuk keluar dari program        
        """)
    elif(role == 'jin_pembangun'):
        print("""
=========== HELP ===========
1. logout
Untuk keluar dari akun yang digunakan 
2. bangun
Untuk membangun candi
3. save
Untuk menyimpan data permainan
4. exit
Untuk keluar dari program
        """)
    elif(role == 'jin_pengumpul'):
        print("""
=========== HELP ===========
1. logout
Untuk keluar dari akun yang digunakan 
2. kumpul
Untuk mengumpulkan resource candi
3. save
Untuk menyimpan data permainan
4. exit
Untuk keluar dari program 
        """)
def F16():
    savefile = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while savefile != "y" or savefile != "n" or savefile != "Y" or savefile != "N":
        savefile = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if savefile == "y" or savefile == "Y":
        print("save")
    else:
        print()
        print("File yang sudah diubah tidak tersimpan.")

        
while True:
    pilihan = input(">>> ")
    if (pilihan == 'login'):
        F01()
    elif (pilihan == 'logout'):
        F02()
    elif (pilihan == 'summonjin'):
        F03()
    elif(pilihan == 'hapusjin'):
        F04()
    elif (pilihan == 'ubahjin'):
        F05()
    elif(pilihan == 'bangun'):
        F06()
    elif(pilihan == 'kumpul'):
        F07()
    elif(pilihan == 'ayamberkokok'):
        F12()
    elif(pilihan == 'help'):
        F15()
    elif (pilihan == 'exit'):
        break
