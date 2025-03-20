#input parameter
lambda_t = float(input("Masukkan nilai λt = "))
m = int(input("Masukkan nilai m = "))

#nilai konstanta e
e = 2.71828 #diketahui pada soal

#menghitung nilai e ** -lambda_t
x = 2.71828 ** -lambda_t

#perhitungan
faktorial = 1
for n in range (m + 1) :
    if n > 0 :
        faktorial *= n
    #menghitung P(N(t)= n)    
    poisson = x * lambda_t ** n / faktorial
    print(f"P(N(t)) = {n} = {poisson}")