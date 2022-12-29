pilihan = "Y"
while pilihan == "Y":
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
    menu = str(input("Masukan menu kopi ="))
    jumlah = int(input("Masukkan jumlah pesanan ="))
    if menu == "1":
        nama_menu = "Kopi Python"
        harga = (15000 * jumlah)
        ppn = int(harga * 0.1)
        if jumlah >= 5:
            diskon = int(harga * 0.2)
            total = int(harga - diskon + ppn)
        else:
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
    else:
        nama_menu = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        total = "-"
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
    pilihan = input("Pilih Y untuk kembali menghitung Y/N =")
