#Tampilan 1

print("********** DAFTAR PAKET DAN ISI **********")
print("*Paket A*")
print("Isi :" "Nasi goreng, Es teh")
print("Harga : 30000\n")
print("*Paket B*")
print("Isi :" "Ayam Bakar, Nasi Putih, Es Jeruk") 
print("Harga : 50000\n")
print("*Paket C*")  
print("Isi :" "Dendeng, Nasi Putih, Es Teh")
print("Harga : 45000\n")
print("*Paket D*")  
print("Isi :" "Ayam Bumbu, Nasi Putih, Mineral") 
print("Harga : 32000\n")
print("*Paket E*")  
print("Isi :" "Soto Betawi, Nasi Putih, Es Jeruk Nipis") 
print("Harga : 55000\n")
print("*Paket F*")  
print("Isi :" "Pecel Ayam, Nasi Uduk, Es Teh") 
print("Harga : 41000\n")
print("*Paket G*")  
print("Isi :" "Chicken Katsu, Kentang Goreng, Mineral") 
print("Harga : 60000\n")
print("*Paket H*") 
print("Isi :" "Chicken Steak, Kentang Goreng, Mineral")
print("Harga : 65000\n")


#Tampilan 2
print("***** LEMBARAN PEMESANAN *****")
nama_customer = input("Masukkan nama customer : ")
no_telepon = int(input("Masukkan nomor telepon customer : "))
alamat = input("Masukkan alamat customer : ")
paket = input("Paket yang dipilih : ")
if paket == "A" :
    isi = "Nasi goreng, Es teh"
    harga = 30000
elif paket == "B" :
    isi = "Ayam Bakar, Nasi Putih, Es Jeruk"
    harga = 50000
elif paket == "C" :
    isi = "Dendeng, Nasi Putih, Es Teh"
    harga = 45000
elif paket == "D" :
    isi = "Ayam Bumbu, Nasi Putih, Mineral"
    harga = 32000
elif paket == "E" :
    isi = "Soto Betawi, Nasi Putih, Es Jeruk Nipis"
    harga = 55000
elif paket == "F" :
    isi = "Pecel Ayam, Nasi Uduk, Es Teh"
    harga = 41000
elif paket == "G" :
    isi = "Chicken Katsu, Kentang Goreng, Mineral"
    harga = 60000
elif paket == "H" :
    isi = "Chicken Steak, Kentang Goreng, Mineral"
    harga = 65000

jumlah = int(input("Jumlah paket yang dipesan : "))
total = harga * jumlah 
pajak = int(total * 10/100) 
biaya_kirim = int(total)
if total < 150000 :
    biaya_pengiriman = 25000
else :
    biaya_pengiriman = 0
total_akhir = (total + pajak + biaya_pengiriman)

#Tampilan 3

print("***** STRUK PEMESANAN *****  \n")
print(f"Nama              : {nama_customer}")
print(f"Nomor Telepon     : {no_telepon}")
print(f"Alamat Pengiriman : {alamat}")
print(f"Detail Pesanan    : Paket {paket}")
print(f"                           {isi}")
print(f"Jumlah            : {jumlah}")
print(f"Total Harga       : Rp.{total}")
print(f"Pajak (10%)       : {pajak}")
print(f"Biaya Pengiriman  : {biaya_pengiriman}")
print(f"Total Akhir       : {total_akhir}")
print("***** SELAMAT MENIKMATI *****")