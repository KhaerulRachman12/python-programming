jumlah_pembeli = int(input("masukan jumlah pembeli:"))

total_harga =0

for i in range(jumlah_pembeli):
    print(f"\nPembeli {i+1}")

    usia_pembeli = int(input("masukan jumlah usia pembeli:"))
    jumlah_tiket = int(input("masukan jumlah tiket:"))

    harga_anak = 30000
    harga_dewasa = 50000
    harga_lansia = 35000

    if usia < 12:
        harga_tiket = harga_anak
    elif 12<= usia <=60:
        harga_tiket = harga_dewasa
    else:
        harga_tiket = harga_lansia

    total_pembeli = harga_tiket*jumlah_tiket
print(f"harga untuk pembeli {i+1}: {total_pembeli}")
total_harga += total_pembeli
print(f"\nTotal harga untuk semua tiket yang dibeli: Rp {total_harga}")