import random
sec = ["Taş","Kağıt","Makas"]


sayac = 0
while True:
    secim = random.choice(sec)   
    kullanici_secim = input("Taş-Kağıt-Makas? ")
    sayac += 1

    if kullanici_secim not in ["Taş", "Kağıt", "Makas"]:
        print("Geçersiz İşlem!")
        continue
    if secim == kullanici_secim:
        print("Berabere")

    elif (kullanici_secim== "Taş" and secim== "Makas") or\
         (kullanici_secim =="Kağıt" and secim=="Taş") or \
         (kullanici_secim=="Makas" and secim=="Kağıt"):
        print(f"Tebrikler,{sayac}. Turda Kazandınız!")
    else:
        print("Kaybettiniz")
    print("Bilgisayar: ", secim)