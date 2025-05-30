def input_data_praktikan():
    praktikan = []
    n = int(input("Masukkan jumlah praktikan dalam shift: "))

    for i in range(n):
        print(f"\nData Praktikan ke-{i+1}")
        data = []
        nama = input("Nama: ")
        nim = input("NIM: ")
        pretest = float(input("Nilai Pretest: "))
        postest = float(input("Nilai Postest: "))
        tugas = float(input("Nilai Tugas/Makalah: "))
        bonus = float(input("Nilai Bonus: "))
        
        data.extend([nama, nim, pretest, postest, tugas, bonus])
        praktikan.append(data)
    
    return praktikan

def hitung_nilai_akhir(praktikan):
    for i in range(len(praktikan)):
        pre = praktikan[i][2]
        post = praktikan[i][3]
        tugas = praktikan[i][4]
        bonus = praktikan[i][5]
        akhir = (0.25 * pre + 0.25 * post + 0.5 * tugas) + bonus
        praktikan[i].append(akhir)  # <- nilai akhir ditambahkan ke list
    return praktikan


def urutkan_dan_peringkat(praktikan):
    for i in range(len(praktikan)):
        for j in range(i + 1, len(praktikan)):
            if praktikan[i][6] < praktikan[j][6]:
                praktikan[i], praktikan[j] = praktikan[j], praktikan[i]
    for i in range(len(praktikan)):
        praktikan[i].append(i + 1)
    
    return praktikan

def tampilkan_ringkas(praktikan):
    print("\n=== TABEL PERINGKAT PRAKTIKAN ===")
    print("{:<3} {:<10} {:<10} {:<12} {:<10}".format("No", "Nama", "NIM", "Nilai Akhir", "Peringkat"))
    for i in range(len(praktikan)):
        print("{:<3} {:<10} {:<10} {:<12} {:<10}".format(
            i + 1, praktikan[i][0], praktikan[i][1], praktikan[i][6], praktikan[i][7]))

# ========== Jalankan Program ==========
praktikan = input_data_praktikan()
praktikan = hitung_nilai_akhir(praktikan)
praktikan = urutkan_dan_peringkat(praktikan)
tampilkan_ringkas(praktikan)