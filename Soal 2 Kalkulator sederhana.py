# buatkan program menerima 2 angka dan operator (+,-,*,/,%), lalu menampilkan hasil operasi

def kalkulator(a, b, operator):
    if operator == '*':return a*b
    elif operator == '+':return a+b
    elif operator == '-':return a-b
    elif operator == '/':return a/b 
    elif operator == '%':return a%b 
    else: print('operator tidak ditemukan.')

a = float(input('Masukkan angka pertama: '))
operator = input('Masukkan Operator: ')
b = float(input('Masukkan angka kedua: '))

print(kalkulator(a,b,operator))