
user = [["Bondowoso", "cintaroro", "bandung_bondowoso"], ["panji", "panji123", "pembangun"]]

# Ubah tipe jin
username = input("Masukkan username jin: ")
a = False
for i in range (2):
    if username == user[i][0]:
        a = True
        indeksUser = i
        break
        
if a == False:
    print("Tidak ada jin dengan username tersebut.")
else:
        if user[indeksUser][2] == "pengumpul":
            konfirmasi = input(f"Jin ini bertipe \"{user[indeksUser][2]}\". Yakin ingin mengubah ke tipe \"Pembangun\"(Y/N)?")
            if konfirmasi == "Y":
                print("Jin telah berhasil diubah.")
                user[indeksUser][2] = "pembangun"
        else:
            konfirmasi = input(f"Jin ini bertipe \"{user[indeksUser][2]}\". Yakin ingin mengubah ke tipe \"Pengumpul\"(Y/N)?")
            if konfirmasi == "Y":
                print("Jin telah berhasil diubah.")
                user[indeksUser][2] = "pengumpul"
print(user)