# Input tiga bilangan
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
bil3 = int(input("Masukkan bilangan ketiga: "))

# Menentukan bilangan terbesar
if bil1 > bil2 and bil1 > bil3:
    terbesar = bil1
elif bil2 > bil3 and bil2 > bil1:
    terbesar = bil2
else:
    terbesar = bil3

# Output hasil
print("Bilangan terbesar adalah:", terbesar)
