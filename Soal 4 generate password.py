#Buat program yang menghasilkan password acak dengan panjang 8 karakter, terdiri dari huruf besar, huruf kecil, dan angka. Contoh output: X7sL2q9P.

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = 8
new_password = generate_password(password_length)
print("Kata sandi baru Anda adalah:", new_password)