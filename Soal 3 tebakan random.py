# komputer memilih angka acak antara 1-20. pengguna harus menebak angka tersebut, beri petunjuk terlalu besar atau terlalu kecil hingga tebakan benar, tampilkan jumlah percobaan.

import numpy as np
angka_random = np.random.randint(1, 20)

index = 0

while True:
    tebakan = int(input('tebak angka : '))
    index +=1
    if tebakan == angka_random:
        print('Tebakan benar..')
        print(f'jumlah percobaan {index}')
        break
    elif tebakan < angka_random:
        print('salah..tebakan terlalu kecil..')
    else: print('salah..tebakan terlalu besar..')

