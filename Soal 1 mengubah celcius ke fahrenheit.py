# soal 1
# anda ingin membantu teman dari amerika memahami suhu di indonesia. buat program yang mengkonversi suhu dari derajat celcius ke derajat fahrenheit. program harus meminta input suhu dalam celcius dan menampilkan hasil konversi.

# mengubah celsius ke fahrenheit
suhu = float(input('masukkan suhu dalam skala celcius: '))
T_Fahrenheit = (suhu * 1.8) + 32
print(f'suhu {suhu} derajat celcius menjadi suhu {T_Fahrenheit} derajat Fahrenheit')