# Buatkan program untuk menentukan hadiah di atas dengan menerima inputan total pembelian pelanggan!

belanja = int(input("masukkan nilai pembelian pelanggan :"))

if belanja > 1500000 and belanja < 5000000 :
    print("anda mendapatkan TV bracket")
elif belanja > 5000000 :
    print("anda mendapatkan sound bar")
else:
    print("tidak ada bonus")