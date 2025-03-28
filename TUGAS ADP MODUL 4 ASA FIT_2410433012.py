m = int(input("Masukkan jumlah baris = "))
n = int(input("Masukkan jumlah kolom = "))

VVIP = 0
VIP = 0
REGULER = 0
EKONOMI = 0


for i in range (m) :
    if i < 2 :
        VVIP += n
    elif i >= 2 and i < 5 :
        VIP += n
    elif i >= 5 and i < 15 :
        REGULER += n
    else :
        EKONOMI += n

#harga per kategori 
harga_vvip = 2500000
harga_vip = 1750000
harga_reguler = 1000000
harga_ekonomi = 750000

kursi_dipesan = ""

print("\nSELAMAT DATANG DI SISTEM RESERVASI TIKET KONSER!")
print("Tampilan Layout Kursi : ")
baris = 1
nomor = 1
while baris <= m:
    kolom = 1
    while kolom <= n:
        print((f"{nomor:3}"), end=" ")
        kolom = kolom + 1
        nomor = nomor + 1
    print()
    baris = baris + 1

#tampilkan harga
print("\nHarga Tiket : ")
print("VVIP    : Rp", harga_vvip)
print("VIP     : Rp", harga_vip)
print("REGULER : Rp", harga_reguler)
print("EKONOMI : Rp", harga_ekonomi)

#input jumlah tiket yang ingin dibeli
jumlah = int(input("\nMasukkan jumlah tiket yang ingin dipesan : "))
for p in range (jumlah) :
    print(f"\nPemesanan ke-{p+1}") 
    nama = input("Masukkan nama anda : ")
    nomor_kursi = str(input("Masukkan nomor kursi yang ingin dipesan : "))
    password = input("Buat password untuk akses konser : ")


    nomor_kursi_int = int(nomor_kursi)
    baris_kursi = (nomor_kursi_int - 1) // n
    kolom_kursi = (nomor_kursi_int - 1) % n

    if "#" + str(nomor_kursi) + "#" in kursi_dipesan:
        print("Maaf, kursi sudah dipesan.")
    else:
        kursi_dipesan = kursi_dipesan + "#" + str(nomor_kursi) + "#"

        if baris_kursi <= 2:
            kategori = "VVIP"
            harga = harga_vvip
            VVIP -= 1
        elif 3<= baris_kursi <= 5:
            kategori = "VIP"
            harga = harga_vip
            VIP -= 1
        elif 6 <=baris_kursi <= 15:
            kategori = "REGULER"
            harga = harga_reguler
            REGULER -= 1
        else:
            kategori = "EKONOMI"
            harga = harga_ekonomi
            EKONOMI -= 1

        #struk pemesanan
        print("\n=== Struk Pemesanan Tiket ===")
        print("Nama       :", nama)
        print("Nomor Kursi:", nomor_kursi)
        print("Kategori   :", kategori)
        print("Harga      : Rp", harga)
        print("Password   :", password)
        print("------------------------------")

        
 #tampilan sisa kursi
print("\nSisa kursi per kategori:")
print("VVIP    :", VVIP)
print("VIP     :", VIP)
print("Reguler :", REGULER)
print("Ekonomi :", EKONOMI)

#layout setelah pemesanan
print("\nLayout Kursi Setelah Pemesanan:")
print("\nTampilan Layout Kursi Setelah Pemesanan:")
print("\nLayout Kursi Setelah Pemesanan:")
baris = 1
nomor = 1
while baris <= m:
    kolom = 1
    while kolom <= n:
        if "#" + str(nomor) + "#" in kursi_dipesan:
            print("  0", end=" ")
        else:
            print(f"{nomor:3}", end=" ")
        kolom += 1
        nomor += 1
    print()
    baris += 1

print("\nTerima kasih telah melakukan reservasi!")
