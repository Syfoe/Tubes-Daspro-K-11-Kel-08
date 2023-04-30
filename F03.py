# Deskripsi : Program untuk Summon Jin

#%%
def summon () :
    import pandas as pd
    df_datajin = pd.read_csv("user.csv",sep='[;]',engine='python')
    hitung_jin = len(df_datajin.axes[0])-2
    if (hitung_jin) < 100:
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
    
        cekjenisjin = False
        while cekjenisjin == False:
            jenisjin=int(input("Masukkan nomor jenis jin yang ingin dipanggil :"))
            if jenisjin==1 :
                print("Memilih jin 'Pengumpul'")
                cekjenisjin=True
            else:
                if jenisjin==2 :
                    print("Memilih jin 'Pembangun'")
                    cekjenisjin=True
                else:
                    print(f"Tidak ada jenis jin bernomor {jenisjin} ")
    
        cek_username = True
        while cek_username == True:
            Usernamejin=str(input("Masukkan username jin :"))
            cek_username=df_datajin['username'].eq(Usernamejin).any()
            if cek_username == True:
                print(f"Username {Usernamejin} sudah diambil!")
            else:
                cek_username = False

        cek_pass = False
        while cek_pass == False:
            Password = str(input("Masukkan password jin :"))
            lengthpass = 0
            for i in Password:
                lengthpass += 1
            if (lengthpass<5) or (lengthpass>25):
                print("Password panjangnya harus 5-25 karakter!")
            else:
                cek_pass = True
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f"Jin {Usernamejin} berhasil dipanggil!")

    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
# %%
