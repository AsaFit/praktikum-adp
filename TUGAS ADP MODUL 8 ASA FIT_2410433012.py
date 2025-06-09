
def baca_baris(file):
    hasil = ""
    while True:
        c = file.read(1)
        if c == "" or c == "\n":
            break
        hasil = hasil + c
    return hasil

def pecah_data(line, pemisah="|"):
    hasil = []
    temp = ""
    i = 0
    while i < len(line):
        if line[i] == pemisah:
            hasil.append(temp)
            temp = ""
        else:
            temp = temp + line[i]
        i = i + 1
    hasil.append(temp)
    return hasil

def konversi_int(s):
    angka = 0
    i = 0
    while i < len(s):
        if s[i] == "0":
            digit = 0
        elif s[i] == "1":
            digit = 1
        elif s[i] == "2":
            digit = 2
        elif s[i] == "3":
            digit = 3
        elif s[i] == "4":
            digit = 4
        elif s[i] == "5":
            digit = 5
        elif s[i] == "6":
            digit = 6
        elif s[i] == "7":
            digit = 7
        elif s[i] == "8":
            digit = 8
        elif s[i] == "9":
            digit = 9
        else:
            return -1
        angka = angka * 10 + digit
        i = i + 1
    return angka

def load_data(nama_file):
    data = {}
    f = None
    try:
        f = open(nama_file, "r")
    except:
        # Kalau file tidak ada, data tetap kosong
        return data

    while True:
        line = baca_baris(f)
        if line == "":
            break
        bagian = pecah_data(line, "|")
        if len(bagian) == 5:
            nomor = bagian[0]
            tanggal = bagian[1]
            keterangan = bagian[2]
            jumlah = konversi_int(bagian[3])
            tipe = bagian[4]
            if jumlah >= 0 and (tipe == "pemasukan" or tipe == "pengeluaran"):
                data[nomor] = {
                    "tanggal": tanggal,
                    "keterangan": keterangan,
                    "jumlah": jumlah,
                    "tipe": tipe
                }
    if f is not None:
        f.close()
    return data

def simpan_data(data, nama_file):
    f = open(nama_file, "w")
    for k in data:
        d = data[k]
        line = k + "|" + d["tanggal"] + "|" + d["keterangan"] + "|" + str(d["jumlah"]) + "|" + d["tipe"] + "\n"
        f.write(line)
    f.close()

def tampilkan_menu():
    print("\n=== PROGRAM PENCATAT KEUANGAN ===")
    print("1. Tambah data keuangan")
    print("2. Hapus data keuangan")
    print("3. Tampilkan semua data")
    print("4. Keluar")

def tampilkan_data(data):
    if len(data) == 0:
        print("Belum ada data keuangan.")
        return
    print("\nNo  Tanggal    Keterangan               Jumlah     Tipe")
    print("-"*55)
    for k in data:
        d = data[k]
        print("{:<4}{:<11}{:<25}{:<10}{}".format(k, d["tanggal"], d["keterangan"], d["jumlah"], d["tipe"]))
    print("-"*55)

def tambah_data(data):
    print("\nTambah Data Keuangan")
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    keterangan = input("Keterangan: ")
    valid_jumlah = False
    while not valid_jumlah:
        jumlah_str = input("Jumlah uang: ")
        jumlah = konversi_int(jumlah_str)
        if jumlah >= 0:
            valid_jumlah = True
        else:
            print("Masukkan angka yang valid!")
    tipe = ""
    while True:
        tipe_input = input("Tipe (pemasukan/pengeluaran): ")
        if tipe_input == "pemasukan" or tipe_input == "pengeluaran":
            tipe = tipe_input
            break
        print("Tipe harus 'pemasukan' atau 'pengeluaran'.")
    nomor = str(len(data) + 1)
    data[nomor] = {
        "tanggal": tanggal,
        "keterangan": keterangan,
        "jumlah": jumlah,
        "tipe": tipe
    }
    print("Data berhasil ditambahkan!")

def hapus_data(data):
    if len(data) == 0:
        print("Belum ada data untuk dihapus.")
        return
    tampilkan_data(data)
    nomor = input("Masukkan nomor data yang ingin dihapus: ")
    if nomor in data:
        konfirmasi = input("Yakin ingin menghapus? (y/n): ")
        if konfirmasi == "y":
            del data[nomor]
            print("Data berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Nomor data tidak ditemukan.")


# Mulai program di sini, langsung jalan tanpa fungsi main()

NAMA_FILE = "data_keuangan.txt"
data_keuangan = load_data(NAMA_FILE)

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_data(data_keuangan)
        simpan_data(data_keuangan, NAMA_FILE)
    elif pilihan == "2":
        hapus_data(data_keuangan)
        simpan_data(data_keuangan, NAMA_FILE)
    elif pilihan == "3":
        tampilkan_data(data_keuangan)
    elif pilihan == "4":
        print("Terima kasih sudah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")