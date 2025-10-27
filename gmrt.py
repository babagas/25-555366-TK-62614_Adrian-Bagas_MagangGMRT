import numpy as np

def kinematic():
    opsi = int(input("ketik 1 untuk forward kinematic , ketik 2 untuk inverse kinematic : "))
    if opsi == 1:
        l1=int(input("masukkan panjang femur (cm): "))
        l2=int(input("masukkan panjang tibia (cm): "))
        a1=int(input("berapa sudut pada servo 1 (derajat): "))
        a2=int(input("berapa sudut pada servo 2 (derajat): "))
        a1_rad = np.deg2rad(a1)
        a2_rad = np.deg2rad(a2)
        rotasi1 = np.array([[np.cos(a1_rad),-np.sin(a1_rad),0],
                        [np.sin(a1_rad),np.cos(a1_rad),0],
                        [0,0,1]])
        posisi1 = np.array([[1,0,l1],
                        [0,1,0],
                        [0,0,1]])
        rotasi2 = np.array([[np.cos(a2_rad),-np.sin(a2_rad),0],
                        [np.sin(a2_rad),np.cos(a2_rad),0],
                        [0,0,1]])
        posisi2 = np.array([[1,0,l2],
                        [0,1,0],
                        [0,0,1]])
        titikakhir = rotasi1 @ posisi1 @ rotasi2 @ posisi2
        print("koordinat titik akhir berada di koordinat (" + str(titikakhir[0,2]) + "," + str(titikakhir[1,2]) + ")")

    elif opsi==2 :
        x = int(input("masukkan koordinat titik akhir pada sumbu x"))
        y = int(input("masukkan koordinat titik akhir pada sumbu y"))
        l1 = int(input("masukkan panjang femur"))
        l2 = int(input("masukkan panjang tibia"))
        a2 = np.arccos((x**2+y**2-l1**2-l2**2)/(2*l1*l2))
        a2_derajat = np.rad2deg(a2)
        a1 = np.arctan(y/x)-np.arctan((l2*np.sin(a2))/(l1+l2*np.cos(a2)))
        a1_derajat = np.rad2deg(a1)
        print("sudut pada servo 1 adalah " + str(a1_derajat) + " derajat dan sudut pada servo ke 2 adalah " + str(a2_derajat) + " derajat")

    else:
        print("opsi tidak valid")

kinematic()