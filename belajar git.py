# def perkalian(a,b,c):
#     return a*b*c

# result = perkalian(11,7,6)
# print(result)    


# nama = input('masukkan nama anda :')
# tahun_lahir = input('masukkan tahun lahir anda :')
# umur = 2025 - int(tahun_lahir)

# print(f'Hallo {nama}, Selamat data di dicoding indonesia. per 2025 umur anda {umur} tahun.')
    
# a = 3
# b = 10

# result = a * b
# print(result) 

# print(a**b)
# print(b//a)

# ketersediaan = ''

# one liner
# if ketersediaan == 'daging ayam':
#     print('ibu akan memasak ayam')
# elif ketersediaan == 'tempe':
#     print('ibu memasak tempe')
# else:
#     print('ibu tidak memasak apapun')

# nilai = int(input('masukkan nilai siswa : '))

# #kondisi 
# if nilai > 90: print('A')
# elif 75 < nilai < 90: print('B') 
# elif 45 < nilai < 75: print('C')
# else: print('D')

#ternary operators
# lulus = True 

# print('Selamat kamu sudah lulus') if lulus else print('Maaf kamu masih belum lulus')


# ketersediaan_ayam = True
# print('ibu memasak ayam') if ketersediaan_ayam else print('ibu memasak tempe')


# # ternary tuples
# lulus = False
# kelulusan = ('perbaiki, anda belum lulus', 'selamat, anda telah lulus')[lulus]
# print(kelulusan)


#contoh perulangan for

# var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in var_list:
#     print(i)

# for i in range(20):
#     print(i)
    
# for i in range(1,15,2):
#     print(i)
    


# contoh perulangan while

counter = 0
while counter <= 7:
    print(counter)
    counter += 1

# nested looping
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)
        
# control flow break
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

# control flow continue
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

# control flow else
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")
    

# control flow pass
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")
    
    
# list comprehensif
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)


angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

#error handling and Exception Handling

    