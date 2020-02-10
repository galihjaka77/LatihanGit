# # 1. comment
# print('halo')
# print('halo')
# print('halo')

# 2. Variabel

# nama = 'andi';
# print(nama);

# usia = 22;
# usia= 32; # interpreter
# print(usia)

# jomblo = True;
# print(jomblo)

# 3. Data Type

# nama = 'andi';
# usia = 22;
# jomblo = True;
# decimal = 3.14

# print(type(nama));
# print(type(usia));
# print(type(jomblo));
# print(type(decimal));


# 4. Input
# nama = input("what's your name? : ");
# print(nama);

# 5. latian 1
# nama = input("siapa nama kamu?  :");
# umur = input("berapa usia kamu?  :");
# kelamin = input("jenis kelamin kamu?  :");
# pekerjaan = input("pekerjaan kamu  :");

# print()
# print('nama :',nama);
# print('umur :',umur);
# print('jenis kelamin :',kelamin);
# print('pekerjaan :',pekerjaan);

#  6. number & arithmatic operators

# usiaandi = 40;
# usiabudi = 20;

# usiaandi += 3;
# #  usiaandi = usiaandi + 3;

# usiabudi *= 4;
# #  usiabudi = usiabudi * 3;

# print('usia andi ditambah 3 =', usiaandi);
# print('usia budi dikali 4 =', usiabudi);

# 7. math module
# import math

# print(math.pi);
# print(math.fabs(-4.7));
# print(math.pow(8,2));
# print(math.sqrt(64));

# # 8. round, Ceil, & floor
# import math

# print(round(4.7)); # dibulatkan
# print(round(4.4));
# print(math.floor(4.7)); # kebawah
# print(math.ceil(4.4)); # keatas

# 9. strings

# x = 'halo dunia';

# print(len(x));
# print(x.index('dunia'));
# print(x.split(' '));
# print(x.lower());
# print(x.upper());
# print(x.capitalize());

# singleQuotes = 'single quotes'
# doubleQuotes = "double quotes"
# combineQuotes = "wrap lot's of other"

# print(singleQuotes)
# print(doubleQuotes)
# print(combineQuotes)

# 10. string indexing
# text = "i'm Baron, nice to meet you";

# print(text[1]);
# print(text[2:]);
# print(text[:4]);
# print(text[2:5]);
# print(text[:]);

# 11. convert strings to numbers 
# angka1 = input("masukkan angka 1 : ");
# angka2 = input("masukkan angka 2 : ");

# print(angka1 + angka2);
# print(int(angka1) + int(angka2));

# angka1 = float(angka1);
# angka2 = float(angka2);

# print(angka1 + angka2);

# 12. adding strins & numbers
# usia = 22;
# nama = 'rizput';

# print(usia + usia);
# print(nama + ' ' + nama);
# print(nama + ' ' + str(usia));

# solve it! 1

# x = 4;
# y = 3;
# z = 2;

# print(x + y)
# print('w =', ((x+y*z)^z) / ((x*y)^z))

#  solve it! 2

# kuadrat = input('silahkan masukkan angka berapapun : ')
# print('kuadrat dari',kuadrat,'=',int(kuadrat)**int(kuadrat))

#  solve it! 3

# import math

# total_hari = 485

# a = int(total_hari) / 360
# b = (int(total_hari) % 360) / 30
# c = (int(total_hari) % 360) % 30

# print(round(a),'Tahun')
# print(math.floor(b),'Bulan')
# print(c,'Hari')

# menghitung_hari = input('masukkan hari : ')
# a = int(menghitung_hari) / 360
# b = (int(menghitung_hari) % 360) / 30
# c = (int(menghitung_hari) % 360) % 30
# print(round(a),'Tahun')
# print(math.floor(b),'Bulan')
# print(c,'Hari')

# solve it! 4
# import docutils.utils.math.latex2mathml

# total_usia = 49
# rasioAndi = 4
# rasioBudi = 10

# usiaAndi = ((rasioAndi/int(rasioAndi+rasioBudi)*int(total_usia)))
# usiaBudi = ((rasioBudi/int(rasioAndi+rasioBudi)*int(total_usia)))

# # print(usiaAndi)
# # print(usiaBudi)

# tambah_usiaAndi = input('tambah berapa tahun untuk andi ?')
# tambah_usiaBudi = input('tambah berapa tahun untuk budi ?')

# print(int(usiaAndi)+ int(tambah_usiaAndi))
# print(int(usiaBudi)+ int(tambah_usiaBudi))

# solve it! 5
# kalimat = input('masukkan kalimat anda :')
# print(kalimat)

# cari = input('masukan huruf yang ingin dicari :')

# hitung = 0

# for item in kalimat:
#     if item == cari:
#         hitung += 1
# print(hitung)

# cara mudah
# text1 = 'halo duniaaaa'

# print('"halo duniaaaa" memiliki huruf "a" sebanyak', text1.count('a'),'buah')

# solve it! 6
# import math

# jarakMobil = 120
# kecepatan_mobilA = 40
# kecepatan_mobilB = 60
# waktu_sekarang = 9

# waktu_tabrakan = float(jarakMobil)/ float(kecepatan_mobilA + kecepatan_mobilB)
# totalWaktu_menit = waktu_tabrakan*60
# a = round(totalWaktu_menit) / 60
# b = int(totalWaktu_menit) % 60
# print(waktu_tabrakan)
# import math

# jarak = input('masukkan jarak total : ')
# kecepatanA = input('masukkan kecepatan A : ')
# kecepatanB = input('masukkan kecepatan B : ')
# waktu = input('jam berapa berangkatnya ? ')

# jumlah = float(jarak) / (float(kecepatanA) + float(kecepatanB))
# jumlahMenit = int(math.floor(jumlah)*60)
# jumlahMenit2 = float(jumlah)*60
# a = int(math.floor(jumlahMenit))/60
# b = jumlahMenit2 % 60
# total = (a,'jam') + (b,'menit')
# print(total)
# print('waktu kemungkinan kedua mobil bertabrakkan adalah',jumlah,'jam dari waktu keberangkatan')
