#71210783
#UG4

import json

data = None

with open('karyawan.json','r') as datafile:
    data = json.load(datafile)

n = int(input('Masukkan jumlah karyawan baru : '))

alamat = []
kolega = []

for i in range(n):
    for j in range(1,n+1):
        nama = input('Masukkan nama : ')
        alamat = input('Masukkan alamat : ')
        klg = input('Masukkan jumlah kolega : ')