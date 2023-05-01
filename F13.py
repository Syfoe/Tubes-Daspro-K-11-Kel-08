import argparse 
import os

def load ( ) :
    parser = argparse.ArgumentParser(description='Validasi folder')
    parser.add_argument('nama_folder', nargs='?', help='nama folder yang akan divalidasi')
    args = parser.parse_args()

    if args.nama_folder is None :
        print(f'Tidak ada nama folder yang diberikan!')
        print(f'Usage: python main.py <nama_folder>')
    else :
        pathfile = os.path.abspath('main.py')
        pathfolder = os.path.dirname(pathfile)
        pathnew = pathfolder + '\\' + args.nama_folder
        mainfolder = os.path.isdir(pathnew)

        if mainfolder == True :
            print(f'Selamat datang di program "Manajerial Candi"')
            print(f'Silahkan masukkan username Anda')
        else :
            print(f'Folder"{args.nama_folder}" tidak ditemukan.')