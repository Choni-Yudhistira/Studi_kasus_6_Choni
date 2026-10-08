import json
import os

nama_file = "studi_kasus_7.json"

if os.path.exists(nama_file) == False:
    with open(nama_file, "w") as file:
        json.dump([], file, indent=4)

while True:
    print("\n=== SISTEM MANAJEMEN INVENTARIS BARANG ===")
    print("1. Lihat Data Barang")
    print("2. Tambah Data Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        with open(nama_file, "r") as file:
            data_barang = json.load(file)

        print("\n=== DATA INVENTARIS BARANG ===")

        if len(data_barang) == 0:
            print("Belum ada data barang.")
        else:
            for barang in data_barang:
                print("Nama Barang :", barang["nama"])
                print("Kategori    :", barang["kategori"])
                print("Stok        :", barang["stok"])
                print("Harga       :", barang["harga"])
                print("-------------------------")

    elif pilihan == "2":
        print("\n=== TAMBAH DATA BARANG ===")

        nama = input("Nama barang    : ")
        kategori = input("Kategori       : ")
        stok = input("Jumlah stok    : ")
        harga = input("Harga barang   : ")

        with open(nama_file, "r") as file:
            data_barang = json.load(file)

        barang_baru = {
            "nama": nama,
            "kategori": kategori,
            "stok": stok,
            "harga": harga
        }

        data_barang.append(barang_baru)

        with open(nama_file, "w") as file:
            json.dump(data_barang, file, indent=4)

        print("Data barang berhasil ditambahkan.")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan menu tidak tersedia.")