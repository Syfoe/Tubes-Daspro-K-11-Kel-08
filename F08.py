# Deskripsi : Program untuk kumpul/bangun

#%%
import pandas as pd
import random

def bahan():
    output = random.randint(0,5)
    return(output)

#def batchkumpul():
def batchkumpul () :
     df_datajin = pd.read_csv("user.csv",sep='[;]',engine='python')
     bahanpasirtotal = 0
     bahanairtotal = 0
     bahanbatutotal = 0

     cek_pengumpul="jin_pengumpul" in df_datajin['role'].unique()
     if cek_pengumpul == False:
          print("Kumpul gagal.  Anda tidak punya jin pengumpul.  Silahkan summon terlebih dahulu.")
     else:
          hitung_jin = df_datajin["role"].value_counts()["jin_pengumpul"]
          print(f"Mengerahkan {hitung_jin} jin untuk mengumpulkan bahan.")

          for i in range (hitung_jin):
               pasir = bahan()
               batu = bahan ()
               air = bahan ()
               bahanpasirtotal += pasir
               bahanbatutotal += batu
               bahanairtotal += air

     print (f"Jin menemukan total {bahanpasirtotal} pasir, {bahanbatutotal} batu, dan {bahanairtotal} air.")
     return(bahanpasirtotal, bahanbatutotal, bahanairtotal)



#def batchbangun():
def batchbangun () :
     bahanpasirtotal, bahanbatutotal, bahanairtotal = batchkumpul ()
     df_datajin = pd.read_csv("user.csv",sep='[;]',engine='python')
     kebutuhanpasirtotal = 0
     kebutuhanairtotal = 0
     kebutuhanbatutotal = 0
     cek_pengumpul="jin_pembangun" in df_datajin['role'].unique()
     if cek_pengumpul == False:
          print("Bangun gagal.  Anda tidak punya jin pembangun.  Silahkan summon terlebih dahulu.")
     else:
          hitung_jin = df_datajin["role"].value_counts()["jin_pembangun"]
          for i in range (hitung_jin):
               pasir = bahan()
               batu = bahan ()
               air = bahan ()
               kebutuhanpasirtotal += pasir
               kebutuhanbatutotal += batu
               kebutuhanairtotal += air
    
     print(f"Mengerahkan {hitung_jin} jin untuk membangun candi dengan total bahan {kebutuhanpasirtotal} pasir, {kebutuhanbatutotal} batu dan {kebutuhanairtotal} air.")

     if kebutuhanpasirtotal <= bahanpasirtotal:
          if kebutuhanbatutotal <= bahanbatutotal:
               if kebutuhanairtotal <= bahanairtotal:
                    #pasir cukup, batu cukup, air cukup 
                    print(f"Jin berhasil membangun total {hitung_jin} candi")
               else:
                    #pasir cukup, batu cukup, air kurang
                    print(f"Bangun gagal.  Kurang {kebutuhanairtotal-bahanairtotal} air.")
          else:
               if kebutuhanairtotal <= bahanairtotal:
                    #pasir cukup, batu kurang, air cukup
                    print(f"Bangun gagal. Kurang {kebutuhanbatutotal-bahanbatutotal} batu.")
               else:
                    #pasir cukup, batu kurang, air kurang
                    print(f"Bangun gagal. Kurang {kebutuhanbatutotal-bahanbatutotal} batu dan {kebutuhanairtotal-bahanairtotal} air.")
     else:
          if kebutuhanbatutotal <= bahanbatutotal:
               if kebutuhanairtotal <= bahanairtotal:
                    #pasir kurang, batu cukup, air cukup
                    print(f"Bangun gagal. Kurang {kebutuhanpasirtotal-bahanpasirtotal} pasir.")
               else:
                    #pasir kurang, batu cukup, air kurang
                    print(f"Bangun gagal. Kurang {kebutuhanpasirtotal-bahanpasirtotal} pasir dan {kebutuhanairtotal-bahanairtotal}.")
          else:
               if kebutuhanairtotal <= bahanairtotal:
                    #pasir kurang, batu kurang, air cukup
                    print(f"Bangun gagal. Kurang {kebutuhanpasirtotal-bahanpasirtotal} pasir dan {kebutuhanbatutotal-bahanbatutotal} batu.")
               else:
                    #pasir kurang, batu kurang, air kurang
                    print(f"Bangun gagal. Kurang {kebutuhanpasirtotal-bahanpasirtotal} pasir, {kebutuhanbatutotal-bahanbatutotal} batu dan {kebutuhanairtotal-bahanairtotal} air.")
                       
    
               
        

# %%
