# angka_1 = 5
# angka_2 = 10
# angka_3 = '10'
# angka_4 = '15'

# print(angka_1 * angka_2)
# print(angka_1 / angka_2)
# print(angka_3 * angka_1)
# print(angka_3 * str(angka_1))
# print(angka_2 % angka_1)

# nama = input('masukan nama anda : ')
# umur = input('masukan umur anda: ')
# jenisKelamin = input('jenis kelamin anda : ')

# print(f'nama saya {nama}, umur saya {umur}, dan saya adalah seorang {jenisKelamin}')
# print('nama saya' + nama + ',' + 'umur' + umur +',' + jenisKelamin )

# import math
# # ceil, pows/**, sqrt
# angka_1 = 5
# angka_2 = 12
# angka_3 = 64

# print(math.ceil(angka_2/angka_1))
# print(math.floor(angka_2/angka_1))
# print(math.sqrt(angka_3))
# print(math.pow(angka_2,5))

# nama = 'Anugrah Nurhamid'
 # nama_split =nama.split('!')[1]

# # print(nama_split.split('#'))
# # print(nama.index('d'))
# # print(len(nama))
# print(nama.lower())
# print(nama.upper())
# print(nama.capitalize())

# singleQuotes = 'single quotes'
# doubleQuotes = "double quotes"
# combineQuotes = "wrap lot's of other"

# a = 5
# b = 6

# temp = a
# a = b
# b = temp

# print(a)
# print(b)

# nama = "i'm Anugrah Nurhamid"
# print(len(nama))
# print(nama[2:5])
# print(nama[:5])
# print(nama[:])
# print(nama[2:])

# solve it! 1
# import math
# x = 4;
# y = 3;
# z = 2;
# w = ((x+y*z) / (x*y))**z

# print(x + y)
# print(w) 

#  solve it! 2

# kuadrat = int(input('silahkan masukkan angka berapapun : '))
# print(f'kuadrat dari {kuadrat} = ' + str(kuadrat**2))

# #  solve it! 3

# import math

# total_hari = 485

# tahun = int(total_hari) / 360
# bulan = (int(total_hari) % 360) / 30
# minggu = ((int(total_hari) % 360) % 30)/7

# print(round(tahun),'Tahun')
# print(math.floor(bulan),'Bulan')
# print(math.floor(minggu), 'minggu')
# print(hari,'Hari')

# import math  
# menghitung_hari = int(input('masukkan hari : '))
# tahun = str(math.floor(menghitung_hari/360))
# bulan = str(math.floor((menghitung_hari%360)/30))
# minggu = str(math.floor(((menghitung_hari%360)%360)/7))
# hari = str(math.floor(((menghitung_hari%360)%30)/7))
# print(tahun + " tahun " + bulan + " bulan " + minggu + " minggu " + hari + " hari ")


# solve it! 5
# text1 = 'halo duniaaaa'

# print('"halo duniaaaa" memiliki huruf "a" sebanyak', text1.count('a'),'buah')

# cara kang uga
# word = input('kata : ')
# cari = input('huruf yang dicari : ')
# print(int(len(word.split(cari)))-1)

# word = 'halo dunia'
# cari = 'a'
# word_split = word.split(cari)
# length_word = len(word_split)
# print(word_split)
# print(length_word-1)

# print(len(word.split(cari))-1)

# solve it! 6
# import math

# jarak = input('masukkan jarak total : ')
# kecepatanA = input('masukkan kecepatan A : ')
# kecepatanB = input('masukkan kecepatan B : ')


# jumlah = float(jarak) / (float(kecepatanA) + float(kecepatanB))
# jumlahMenit = int(math.floor(jumlah)*60)
# jumlahMenit2 = float(jumlah)*60
# a = int(math.floor(jumlahMenit))/60
# b = jumlahMenit2 % 60
# total = (a,'jam') + (b,'menit')
# print(total)
# print('waktu kemungkinan kedua mobil bertabrakkan adalah',jumlah,'jam dari waktu keberangkatan')

# cara kang uga

# import math

# jarak_benda     = int(input('jarak antara dua benda : '))
# kecepatan_A     = int(input('kecepatan benda A : '))
# kecepatan_B     = int(input('kecepatan benda B : '))
# jam_berangkat   = int(input('jam keberangatan : '))
# menit_berangkat = int(input('menit keberangkatan : '))

# waktu_tabrakan_dalam_menit = ((jarak_benda)/((kecepatan_A)+(kecepatan_B)))*60
# print(str(waktu_tabrakan_dalam_menit) + 'menit')

# jam = math.floor(waktu_tabrakan_dalam_menit/60) + jam_berangkat
# menit = (menit_berangkat +(waktu_tabrakan_dalam_menit%60))%60
# print(f'waktu A & B bertabrakan adalah jam {jam}.{menit} WIB')

