import os, sys,time



print(time.timezone)
os.system("cls")
os.system("color b")
print("|=====================================================================|")
print("|---------------------------------------------------------------------|")
print("|                   Program Penghitung Bangun Ruang                   |")
print("|---------------------------------------------------------------------|")
print("|=====================================================================|")
print("| 1. Kubus                                                            |")
print("| 2. Balok                                                            |")
print("| 3. Prisma Segi Tiga                                                 |")
print("| 4. Prisma Segi Empat                                                |")
print("|---------------------------------------------------------------------|")
Pilihan = int(input("Masukkan Pilihan Anda : "))




if Pilihan ==1:

    print("|=====================================================================|")
    print("|---------------------------------------------------------------------|")
    print("| 1. Volume Kubus                                                     |")
    print("| 2. Luas Kubus                                                       |")
    print("| 3. Keliling Kubus                                                   |")
    print("|---------------------------------------------------------------------|")
    PilihanKubus = int(input("Masukkan Opsi Anda : "))
    if PilihanKubus==1:
        Sisi = float(input("Masukkan Panjang Sisi : "))
        VolumeKubus = Sisi ** 3
        print("Volumenya : ",VolumeKubus,"\nRumusnya Adalah : Sisi x Sisi x Sisi")
    if PilihanKubus==2:
        Sisi = float(input("Masukkan Panjang Sisi : "))
        LuasKubus = 6*Sisi**2
        print("Luasnya : ",LuasKubus,"\nRumusnya Adalah : 6 x Sisi x Sisi")

    if PilihanKubus == 3:
        Sisi = float(input("Masukkan Panjang Sisi : "))
        KelilingKubus = 12*Sisi
        print("Kelilingnya Adalah : ",KelilingKubus,"\nRumusnya Adalah : 12 x Sisi")

    time.sleep(1.5)
    Lagi = input("Mencoba Lagi? Ya Atau Tidak : ")
    if Lagi == "Ya":
        os.system("python Main.py")
    if Lagi == "ya":
        os.system("python Main.py")
    if Lagi == "YA":
        os.system("python Main.py")
    if Lagi == "Tidak":
        sys.exit()
    if Lagi == "tidak":
        sys.exit()
    if Lagi == "TIDAK":
        sys.exit()




if Pilihan ==2:
    print("|=====================================================================|")
    print("|---------------------------------------------------------------------|")
    print("| 1. Volume Balok                                                     |")
    print("| 2. Luas Balok                                                       |")
    print("| 3. Keliling Balok                                                   |")
    print("|---------------------------------------------------------------------|")
    PilihanBalok = int(input("Masukkan Opsi Anda : "))
    if PilihanBalok==1:
        Panjang = float(input("Masukkan Panjang Balok : "))
        Lebar = float(input("Masukkan Lebar Balok : "))
        Tinggi = float(input("Masukkan Tinggi Balok : "))
        VolumeBalok = Panjang*Lebar*Tinggi
        print("Volumenya Adalah : ",VolumeBalok,"\nRumusnya Adalah : Panjang x Lebar x Tinggi")
    if PilihanBalok==2:
        Panjang = float(input("Masukkan Panjang Balok : "))
        Lebar = float(input("Masukkan Lebar Balok : "))
        Tinggi = float(input("Masukkan Tinggi Balok : "))
        LuasBalok1 = Panjang*Lebar
        LuasBalok2 = Panjang*Tinggi
        LuasBalok3 = Lebar*Tinggi
        LuasBalok4 = LuasBalok1+LuasBalok2+LuasBalok3
        LuasBalok = 2*LuasBalok4
        print("Luasnya Adalah : ",LuasBalok,"\nRumusnya Adalah : 2 x (Panjang x Tinggi) + (Panjang x Lebar) + (Tinggi x Lebar)")
    if PilihanBalok==3:
        Panjang = float(input("Masukkan Panjang Balok : "))
        Lebar = float(input("Masukkan Lebar Balok : "))
        Tinggi = float(input("Masukkan Tinggi Balok : "))
        KelilingBalok = 4*(Panjang+Lebar+Tinggi)
        print("Kelilingnya Adalah : ",KelilingBalok,"\nRumusnya Adalah : 4 x Panjang + Lebar + Tinggi")



    time.sleep(1.5)
    Lagi = input("Mencoba Lagi? Ya Atau Tidak : ")
    if Lagi == "Ya":
        os.system("python Main.py")
    if Lagi == "ya":
        os.system("python Main.py")
    if Lagi == "YA":
        os.system("python Main.py")
    if Lagi == "Tidak":
        sys.exit()
    if Lagi == "tidak":
        sys.exit()
    if Lagi == "TIDAK":
        sys.exit()













































