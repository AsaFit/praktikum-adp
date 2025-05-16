# List untuk menyimpan data mahasiswa
nim_mahasiswa = []
nama_mahasiswa = []
nilai_mahasiswa = []

while True:
    print("== Menu Utama ==")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")

    pilihan = input("Pilih Menu : ")
    print()

    if pilihan == "1":
        print("---- Tambah Data Mahasiswa ----")
        nim = input("NIM Mahasiswa : ")
        nama = input("Nama Mahasiswa : ")
        nilai = float(input("Nilai Mahasiswa : "))

        nim_mahasiswa.append(nim)
        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)
        print("\nData berhasil ditambahkan!\n")

    elif pilihan == "2":
        print("---- Hapus Data Mahasiswa ----")
        hapus_nim = input("NIM Mahasiswa yang akan dihapus : ")

        nim_baru = []
        nama_baru = []
        nilai_baru = []
        ditemukan = False

        for i in range(len(nim_mahasiswa)):
            if nim_mahasiswa[i] != hapus_nim:
                nim_baru.append(nim_mahasiswa[i])
                nama_baru.append(nama_mahasiswa[i])
                nilai_baru.append(nilai_mahasiswa[i])
            else:
                ditemukan = True

        if ditemukan:
            nim_mahasiswa = nim_baru
            nama_mahasiswa = nama_baru
            nilai_mahasiswa = nilai_baru
            print("\nData berhasil dihapus!\n")
        else:
            print("\nData tidak ditemukan!\n")

    elif pilihan == "3":
        print("---- Tampilkan Data Mahasiswa ----")
        if len(nim_mahasiswa) > 0:
            # Buat salinan data untuk diurutkan berdasarkan nilai
            data_salinan = []
            for i in range(len(nim_mahasiswa)):
                data_salinan.append([nim_mahasiswa[i], nama_mahasiswa[i], nilai_mahasiswa[i]])

            # Bubble sort berdasarkan nilai (nilai descending)
            for i in range(len(data_salinan)):
                for j in range(i + 1, len(data_salinan)):
                    if data_salinan[i][2] < data_salinan[j][2]:
                        x = data_salinan[i]
                        data_salinan[i] = data_salinan[j]
                        data_salinan[j] = x

            # Tampilkan hasil
            print(f"{'NIM':<10} | {'Nama':<15} | {'Nilai':<5}")
            print("----------------------------------------")
            for data in data_salinan:
                print(f"{data[0]:<10} | {data[1]:<15} | {data[2]:<5}")
            print()
        else:
            print("Belum ada data mahasiswa.\n")

    elif pilihan == "4":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid.\n")