from ast import If


a = int(input("masukkan angka 1: "))
b = int(input("masukkan angka 2: "))
tambah = a + b
kurang = a - b
kali = a * b
bagi = a / b

print("Silahkan pilih operasi dibawah ini")
print("[1] Penambahan")
print("[2] Pengurangan")
print("[3] Pengkalian")
print("[4] Pembagian")

pilih = (input("Masukkan Pilihan : "))

if (pilih == "1"):
    print("Hasil dari penambahan adalah = ", tambah)
elif (pilih == "2"):
    print("Hasil dari pengurangan adalah = ", kurang)
elif (pilih == "3"):
    print("Hasil dari pengkalian adalah = ", kali)
elif (pilih == "4"):
    print("Hasil dari pembagian adalah = ", bagi)
elif (pilih > "4"):
    print("Angka Yang anda masukkan salah !")
elif (pilih < "1"):
    print("Angka Yang anda masukkan salah !")
