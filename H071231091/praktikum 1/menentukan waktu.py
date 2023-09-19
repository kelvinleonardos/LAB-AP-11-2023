detik = float(input('masukkan angka detik: '))

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

# Menampilkan hasil konversi dalam format jam:menit:detik
print(f"{jam:02d}:{menit:02d}:{detik:02d}")

