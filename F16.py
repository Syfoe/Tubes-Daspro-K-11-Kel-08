def save():
    print()
    
def exit():
    savefile = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while savefile != "y" or savefile != "n" or savefile != "Y" or savefile != "N":
        savefile = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if savefile == "y" or savefile == "Y":
        save()
    else:
        print()
        print("File yang sudah diubah tidak tersimpan.")