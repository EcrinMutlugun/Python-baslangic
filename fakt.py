# For Döngüsü İle Faktöriyel Hesabı:
# while True:
#     try:
#         sayi = int(input("Lütfen bir sayı giriniz: "))
#     except ValueError:
#         print("Lütfen yalnızca sayı girin! ")
#         continue

#     fakt = 1
#     i = 1
#     for i in range(1,sayi+1):
#         fakt *= i
#         i += 1
#     print(f"{sayi}! = ",fakt)

# While Döngüsü İle Faktöriyel Hesabı:
# while True:
#     try:
#         sayi = int(input("Lütfen bir sayı girin: "))
#     except ValueError:
#         print("Lütfen yalnızca sayı girin! ")
#         continue

#     i = 2
#     fakt = 1
#     while i <= sayi:
#         fakt *= i
#         i += 1
#     print(f"{sayi}! = {fakt}")

# Fonksiyon İle Faktöriyel Hesabı:
def fakt(n):
    sonuc = 1
    for i in range(1,n+1):
        sonuc *= i
    return sonuc

while True:
    try:
        sayi = int(input("Lütfen bir sayı giriniz: "))
    except ValueError:
        print("Lütfen yalnızca sayı girin! ")
        continue
    print(f"{sayi}! = {fakt(sayi)}")