#31082022

#71210783
#UG1

from ssl import OP_SINGLE_DH_USE


def kalkulator():
    print("Ketik Q jika sudah selesai.")
    print("pilih : (1)Penjumlahan, (2)Pengurangan, (3)Pembagian, (4)Perkalian.")

    opsi = input("Masukkan pilihan : ")

    if opsi == "Q":
        global status
        status = False
        return

    a = int(input("a : "))
    b = int(input("b : "))

    if opsi == "1":
        return a+b
    elif opsi == "2":
        return a-b
    elif opsi == "4":
        return a*b
    elif opsi == "3":
        return a/b
    else:
        return "Invalid input"


status = True
while status == True:
    print()
    x = kalkulator()

    if x != None:
        print(x)