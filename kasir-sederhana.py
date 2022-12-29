# inisialisasi variabel pilihan dengan nilai "y"
# ini akan digunakan sebagai kondisi looping
pilihan = "y"

# lakukan looping selama pilihan bernilai "y"
while pilihan == "y":

# Tampilkan daftar menu kopi yang tersedia di warung
    print("""
=======================================
=============Warung Python=============
=======================================
========List Menu Warung Python========
=======================================
1. Kopi Python : Rp 11.000
2. Kopi Anaconda : Rp 12.000
3. Kopi Streamlit : Rp 11.000
4. Kopi Github : Rp 14.000
=======================================
""")
    # minta pengguna memasukkan pilihan menu kopi
    menu = str(input("Masukan menu kopi ="))
    jumlah = int(input("Masukkan jumlah pesanan ="))

    # Lakukan perhitungan biaya berdasarkan pilihan menu kopi
    if menu == "1":
        nama_menu = "Kopi Python"
        harga = (15000 * jumlah)
        ppn = int(harga * 0.1)
        if jumlah >= 5:

            # Berikan diskon 20% jika jumlah pesanan lebih dari 5
            diskon = int(harga * 0.2)
            total = int(harga - diskon + ppn)
        else:

            # Jika jumlah pesanan kurang dari 5, tidak ada diskon
            diskon = 0
            total = int(harga + ppn)
    elif menu == "2":
        nama_menu = "Kopi Anaconda"
        harga = (17000 * jumlah)
        ppn = int(harga * 0.1)
        if jumlah >= 5:
            diskon = int(harga * 0.2)
            total = int(harga - diskon + ppn)
        else:
            diskon = 0
            total = int(harga + ppn)
    elif menu == "3":
        nama_menu = "Kopi Streamlit"
        harga = int(19000 * jumlah)
        ppn = int(harga * 0.1)
        diskon = 0
        total = int(harga + ppn)
    elif menu == "4":
        nama_menu = "Kopi Github"
        harga = int(21000 * jumlah)
        ppn = int(harga * 0.1)
        diskon = 0
        total = int(harga + ppn)
    # Jika pilihan menu salah, inisialisasi nama menu, harga, ppn, dan diskon dengan "-"
    else:
        # Tampilkan pesan error jika pilihan menu salah
        nama_menu = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        total = "-"

    # Tampilkan rincian pembelian kopi ke pengguna    
    print("=======================================")
    print("=============Warung Python=============")
    print("=======================================")
    print("Menu :", nama_menu)
    print("Jumlah Pesan :", jumlah)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN 10% :", ppn)
    print("=======================================")
    print("Jumlah Bayar :", total)
    print("=======================================")
    print("=============Warung Python=============")
    print("==============Terimakasih==============")
    # Minta pengguna memasukkan pilihan untuk kembali menghitung atau keluar dari program
    pilihan = input("Pilih y untuk kembali menghitung y/n =")
