from datetime import datetime

# Input nama dan tahun lahir
nama = input("Masukkan nama Anda: ")
tahun_lahir = int(input("Masukkan tahun lahir Anda: "))

# Mendapatkan tahun sekarang
tahun_sekarang = datetime.now().year

# Menghitung umur
umur = tahun_sekarang - tahun_lahir

# Menampilkan hasil
print(f"Halo {nama}, umur Anda adalah {umur} tahun.")
