print("=== PROGRAM HITUNG JARAK TITIK ===")

n = int(input("Masukkan jumlah titik : "))
titik = []

i = 0
while i < n:
    print("Titik ke-" + str(i+1))
    # validasi input x (boleh desimal dan negatif)
    valid = 0
    while valid == 0:
        x_input = input("Masukkan nilai x : ")
        j = 0
        tanda_negatif = 0
        titik_desimal = 0
        if x_input != "":
            if x_input[0] == "-":
                tanda_negatif = 1
                j = 1
            while j < len(x_input):
                if x_input[j] == ".":
                    titik_desimal = titik_desimal + 1
                    if titik_desimal > 1:
                        break
                elif x_input[j] < "0" or x_input[j] > "9":
                    break
                j = j + 1
    
                valid = 1
        if valid == 0:
            print("  Input x tidak valid! Harus berupa angka.")

    x = float(x_input)

    # validasi input y (boleh desimal dan negatif)
    valid = 0
    while valid == 0:
        y_input = input("Masukkan nilai y : ")
        j = 0
        tanda_negatif = 0
        titik_desimal = 0
        if y_input != "":
            if y_input[0] == "-":
                tanda_negatif = 1
                j = 1
            while j < len(y_input):
                if y_input[j] == ".":
                    titik_desimal = titik_desimal + 1
                    if titik_desimal > 1:
                        break
                elif y_input[j] < "0" or y_input[j] > "9":
                    break
                j = j + 1
            if j == len(y_input) and not (y_input == "-" or y_input == "."):
                valid = 1
        if valid == 0:
            print("  Input y tidak valid! Harus berupa angka.")

    y = float(y_input)

    titik.append([x, y])
    i = i + 1

# menampilkan titik
print("\nDaftar titik:")
i = 0
while i < n:
    print("  Titik", i+1, ":", titik[i])
    i = i + 1

# menghitung jarak
print("\nJarak antar titik:")
i = 0
while i < n:
    j = i + 1
    while j < n:
        dx = titik[j][0] - titik[i][0]
        dy = titik[j][1] - titik[i][1]
        jarak = (dx*dx + dy*dy)**0.5
        print("  Jarak Titik", i+1, "ke", j+1, "=", jarak)
        j = j + 1
    i = i + 1
