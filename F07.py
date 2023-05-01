import random

# Menggunakan Phyton Random Library
def kumpul(user):
    if user == "jin pengumpul":
        pasir = random.randint(0, 5)
        batu = random.randint(0, 5)
        air = random.randint(0, 5)
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    else:
        print("Maaf anda tidak memiliki akses, command ini hanya dapat digunakan oleh Jin Pengumpul")
