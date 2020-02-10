# # soal B

# # Nomor 1
data_asli = [71,70,73,70,70,69,70,72,71,300,71,69]

# # sort data
# # # cara 1
# a = sorted(data_asli)

# # # cara 2
# # def sort_angka(angka):
# #     for i in range(len(data_asli)):
# #         for j in range(i+1,len(data_asli)):
# #             if data_asli[i] > data_asli[j]:
# #                 data_asli[i], data_asli[j] = data_asli[j], data_asli[i]

# #     return data_asli

# # print(sort_angka(data_asli))

# # Nomor 2
# def cari_median(isi_list):
#     if len(isi_list) % 2 == 0:
#         median = (isi_list[len(isi_list)//2] + isi_list[len(isi_list)//2 - 1])/2
#     else :
#         median = isi_list[len(isi_list)//2]

#     return median

# # nomor 3
# def quartal1(list_data):
#     if len(list_data) % 2 == 0:
#         q1 = (list_data[len(list_data)//4] + list_data[len(list_data)//4 - 1])/2
#     else :
#         q1 = list_data[len(list_data)//4]
#     return q1

# def quartal3(list_data):
#     if len(list_data) % 2 == 0:
#         q3 = (list_data[-(len(list_data)//4)] + list_data[-(len(list_data)//4 + 1)])/2
#     else :
#         q3 = list_data[len(list_data)*3//4]
#     return q3
# # nomor 4
# iqr = quartal3(a) - quartal1(a)

# # nomor 5

# lwr_lmt = quartal1(a) - 1.5*iqr

# upp_lmt = quartal3(a) + 1.5*iqr

# def remove_outliner(list1):
#     for i in list1:
#         if i < lwr_lmt or upp_lmt < i:
#             list1.remove(i)
#             print(list1)
#     return list1


# remove_outliner(a)

# print(f'data asli = {data_asli}')
# print(f'data setelah di sort = {a}')
# print('setengah data pertama = ' + str(a[:len(a)//2]))
# print('setengah data pertama = ' + str(a[len(a)//2:]))
# print(f'q1 adalah = {quartal1(a)}')
# print(f'q1 adalah = {quartal3(a)}')
# print(f'lower limit adalah = {lwr_lmt}')
# print(f'lower limit adalah = {upp_lmt}')
# print(f'Data yang tidak outliner = {remove_outliner(a)}')

# # soal B
kalimat = 'budi pergi ke pasar'
kalimat1 = 'purwadhika'
# vowels = 'a','i','u','e','o'
# z = 0
# for i in kalimat1:
#     if i == 'a':
#         z += 1
#     elif i == 'i':
#         z += 1
#     elif i == 'u':
#         z += 1
#     elif i == 'e':
#         z += 1
#     elif i == 'o':
#         z += 1
# print('countVowel("purwadhika")--> ' + str(z))
        
# # soal c
list1 = [[3,2,1],[4,6,5],[],[9,7,8]]
list2 = [[3,4,2,1],[1,2,3],[5,4,3,1]]

# z = []
# for i in list(list1):
#     z += i
# z.sort()
# print(z)

# # soal D
countWords1 = 'jangan jangan kamu adalah aku'

# pisah = countWords.split(' ')

# kata1 = countWords.count('jangan')
# kata2 = countWords.count('kamu')
# kata3 = countWords.count('adalah')
# kata4 = countWords.count('aku')

# print(f"""
# jumlah kata "jangan" ada sebanyak {kata1}
# jumlah kata "jangan" ada sebanyak {kata2}
# jumlah kata "jangan" ada sebanyak {kata3}
# jumlah kata "jangan" ada sebanyak {kata4}
# """)



# # cara kang uga
def remove_outlier(data):
    dataSorted = sorted(data)
    mid = len(data)//2
    data1 = dataSorted[0:mid]
    data3 = dataSorted[-mid:]
    q1 = data1[len(data1)//2] if len(data1) % 2 != 0 else (data1[len(data1)//2] + data1[len(data1)//2-1])/2
    q3 = data1[len(data3)//2] if len(data1) % 2 != 0 else (data3[len(data1)//2] + data3[len(data1)//2-1])/2
    iqr = q3 -q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr
    data_no_outlier = []
    for item in dataSorted :
        if item > lower_limit and item < upper_limit:
            data_no_outlier.append(item)
    print(f'data asli adalah = {data}')
    print(f'data setelah di sorted = {dataSorted}')
    print(f'setengah data pertama = {data1}')
    print(f'setengah data pertama = {data3}')
    print(f'q1 adalah = {q1}')
    print(f'q3 adalah = {q3}')
    print(f'lower limmit adalah = {lower_limit}')
    print(f'upper limmit adalah = {upper_limit}')
    print(f'data yang tidak outlier = {data_no_outlier}')

def countVowel(data):
    jumlahVowels = 0
    vowels = ['a','i','u','e','o']
    for item in data:
        if (item.lower() in vowels):
            jumlahVowels += 1
    print(jumlahVowels)

# countVowel(kalimat)
# countVowel(kalimat1)

def given(array):
    tempList = []
    for i in array:
        for element in i:
            tempList.append(element)
    tempList.sort()
    print(tempList)

# given(list1)
# given(list2)

def countWords(words):
    wordList = words.split(' ')
    countWords = {}
    for item in wordList:
        if (item in countWords.keys()):
            countWords[item] += 1
        else:
            countWords[item] = 1
    for key,value in countWords.items():
        print(f"jumlah kata '{key.capitalize()}' ada sebanyak {value}")


countWords(countWords1)