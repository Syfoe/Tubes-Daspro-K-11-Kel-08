import os
namaFolder = input("Masukkan nama folder: ")
pathFolder = ""
for i in range(len(namaFolder)):
    if i == "/":
        if os.path.exists(pathFolder) == False:
            print(f"Membuat folder {pathFolder}...")
            os.mkdir(pathFolder)
        pathFolder += namaFolder[i]
if os.path.exists(pathFolder) == False:
            print(f"Membuat folder {pathFolder}...")
            os.mkdir(pathFolder)