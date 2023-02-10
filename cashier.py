# -*- coding: utf-8 -*-
"""Cashier_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1llVQ9NFzOMRbwMPephMAFP-LrmRzw4p1
"""

from tabulate import tabulate
import pandas as pd

class Transaksi:
  def __init__(self):
    '''
    Insialisasi class Transaksi
    trans_dict = menyimpan data transaksi (dict)
    valid_trans = mengecek valid tidaknya transaksi
    '''

    self.trans_dict = dict()
    self.valid_trans = True

  
  def add_item(self, nama, jumlah, harga):
    '''
    Menambahkan item ke dictionary
    nama = nama item
    jumlah = jumlah item
    harga = harga item
    '''
    #cek tipe data
    if type(jumlah)!=int:
        print("Jumlah harus berupa angka")

    #cek tipe data
    elif type(harga)!=int:
        print("Harga harus berupa angka")

    else:
    #memasukan data
        dict_add = {nama: [jumlah, harga, jumlah*harga]}
        self.trans_dict.update(dict_add)
        print(f"Item yang dibeli adalah {nama} sejumlah {jumlah} dengan harga Rp {harga}")


  def update_item_name(self, nama, nama_baru):
    '''
    Mengubah nama item di dictionary
    nama = nama lama
    nama_baru = nama baru
    '''

    baru = self.trans_dict[nama]
    self.trans_dict.pop(nama)
    self.trans_dict.update({nama_baru: baru})
    self.print_order()

    #print pesan jika perubahan benar
    print(f"Mengubah {nama} menjadi {nama_baru}")


  def update_item_qty(self, nama, jumlah_baru):
    '''
    Mengubah nama item di dictionary
    nama = nama dengan jumlah barang sebelumnya
    jumlah_baru = jumlah baru 
    '''

    #cek tipe data
    if type(jumlah_baru)!=int:
        print("Jumlah barang harus berupa angka!")

    else:
        self.trans_dict[nama][0] = jumlah_baru
        self.trans_dict[nama][2] = jumlah_baru*self.trans_dict[nama][1]
        self.print_order()
        #print pesan jika perubahan benar
        print(f"Mengubah jumlah item {nama} menjadi {jumlah_baru}")


  def update_item_price(self, nama, harga_baru):
    '''
    Mengubah harga item
    nama = nama item yang akan dirubah harganya
    nama_baru = nama item dengan harga baru
    '''

    #cek tipe data
    if type(harga_baru)!=int:
        print("Harga barang harus berupa angka")

    else:
        self.trans_dict[nama][1] = harga_baru
        self.trans_dict[nama][2] = harga_baru*self.trans_dict[nama][0]
        self.print_order()
        #print pesan jika perubahan benar
        print(f"Mengubah harga item {nama} menjadi {harga_baru}")


  def delete_item(self,nama):
    '''
    Menghapus item dari dict
    '''

    try:
        self.trans_dict.pop(nama)
        print(f"Menghapus pesanan {nama}")
        print(" ")
        self.print_order()

    #print jika item tidak ditemukan
    except KeyError:
        print(f"{nama} tidak ada dalam daftar pesanan")


  def reset_transaction(self):
    '''
    Menghapus semua item di dict
    '''

    self.trans_dict = self.trans_dict.clear
    #print data dihapus
    print("Semua item berhasil dihapus")


  def print_order(self):
    '''
    Menampilkan semua item di dict
    '''

    try:
        table_trans = pd.DataFrame(self.trans_dict)
        headers = ["Nama Item", "Jumlah Item", "Harga/item", "Total Harga"]
        print(tabulate(table_trans, headers, tablefmt="github"))

    #print jika tidak ada item
    except:
        print("Belum ada pemesanan")


  def check_order(self):
    '''
    Menampilakn pesanan dan validitas
    '''

    try:
        table_trans = pd.DataFrame(self.trans_dict)
        headers = ["Nama Item", "Jumlah Item", "Harga/item", "Total Harga"]
        print(tabulate(table_trans, headers, tablefmt="github"))

        cek = 0

        #Mengecek jika jumlah lebih dari 0
        while cek<2:
            for data in table_trans[cek]:
                if data <= 0:
                  self.valid_trans = False
            cek+= 1

        if self.valid_trans:
            print("Pemesanan sudah benar")

        else:
            print("Terdapat kesalahan input data")

    except ValueError:
          print("Belum ada pemesanan")
      

  def total_price(self):
    '''
    Menampilkan semua pesanan dan total belanja
    '''

    #menjalankan method
    self.check_order
    if self.valid_trans:

        #total belanja
        total_belanja = 0
        for item in self.trans_dict:
            total_belanja += self.trans_dict[item][2]

        #diskon 5%
        if total_belanja >200_000:
            diskon = int(total_belanja*0.05)
            total_belanja = int(total_belanja - diskon)
            print(f"Total belanja Anda sebesar {total_belanja}. Anda mendapatkan diskon 5% sebesar {diskon}")

        #diskon 8%
        elif total_belanja >300_000:
            diskon = int(total_belanja*0.08)
            total_belanja = int(total_belanja - diskon)
            print(f"Total belanja Anda sebesar {total_belanja}. Anda mendapatkan diskon 8% sebesar {diskon}")

        #diskon 10%
        elif total_belanja >500_000:
            diskon = int(total_belanja*0.1)
            total_belanja = int(total_belanja - diskon)
            print(f"Total belanja Anda sebesar {total_belanja}. Anda mendapatkan diskon 10% sebesar {diskon}")

        else:
            print(f"Total belanja Anda sebesar {total_belanja}")

transaksi1 = Transaksi()
transaksi1.add_item("Ayam Goreng", 2, 20000)
transaksi1.add_item("Pasta Gigi", 3, 15000)

transaksi1.delete_item("Pasta Gigi")

transaksi1.reset_transaction()

transaksi1 = Transaksi()
transaksi1.add_item("Ayam Goreng", 2, 20000)
transaksi1.add_item("Pasta Gigi", 3, 15000)
transaksi1.add_item("Mainan Mobil", 1, 200000)
transaksi1.add_item("Mie Instan", 5, 3000)

transaksi1.total_price()

transaksi1.update_item_name("Ayam Goreng", "Ayam Rebus")
