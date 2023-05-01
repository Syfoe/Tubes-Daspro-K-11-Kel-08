# Deskripsi : Program untuk ambil laporan candi

#%%
import pandas as pd
def laporanjin () :
    df_datacandi = pd.read_csv("candi.csv",sep='[;]',engine='python')

    Total_candi = df_datacandi.shape[0]
    print (f"Total Candi : {Total_candi}")

    Total_pasir = df_datacandi['pasir'].sum()
    print(f"Total Pasir yang digunakan : {Total_pasir}")

    Total_batu = df_datacandi['batu'].sum()
    print(f"Total Batu yang digunakan : {Total_batu}")

    Total_air = df_datacandi['air'].sum()
    print(f"Total Air yang digunakan : {Total_air}")

    if Total_candi == 0:
        ID_Candi_termahal=0
        ID_Candi_termurah=0
        Candi_termahal=0
        Candi_termurah=0
    else:
        Candi_termahal = 0
        ID_Candi_termahal = 0
        Candi_termurah=(df_datacandi.loc[0,"pasir"]*10000)+(df_datacandi.loc[0,"batu"]*15000)+(df_datacandi.loc[0,"air"]*7500)
        ID_Candi_termurah=df_datacandi.loc[0,"id"]

        for i in range (Total_candi):
            Hargacandi = (df_datacandi.loc[i,"pasir"]*10000)+(df_datacandi.loc[i,"batu"]*15000)+(df_datacandi.loc[i,"air"]*7500)
            print(f"Harga candi : {Hargacandi}")
            if Candi_termahal<Hargacandi:
                Candi_termahal=Hargacandi
                ID_Candi_termahal = df_datacandi.loc[i,"id"]
            if Candi_termurah>Hargacandi:
                Candi_termurah=Hargacandi
                ID_Candi_termurah = df_datacandi.loc[i,"id"]

    print(f"ID Candi Termahal : {ID_Candi_termahal} (Rp {Candi_termahal:,})")
    print(f"ID Candi Termurah : {ID_Candi_termurah} (Rp {Candi_termurah:,})")

# %%
