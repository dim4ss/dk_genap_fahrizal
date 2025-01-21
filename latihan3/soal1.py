# Buatlah program untuk menghitung nilai akhir. Program menerima input nilai UTS, UAS dan nilai Tugas & Absensi!
print("Mata kuliah “Bahasa BASICA” pada universitas LING LUNG mempunyai aturan penilaian sebagai berikut")
UTS = float(input("masukkan nilai UTS :"))
UAS = float(input("masukkan nilai UAS :"))
tugas = float(input("masukkan nilai tugas & absensi :"))

# mengecek
nilai_akhir = (0.3 * UTS) + (0.5 * UAS) + (0.2 * tugas)

# hasil
print("nilai akhir",nilai_akhir)
