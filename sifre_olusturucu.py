import random
import string 
while True:
    try:
        n = int(input("Şifreniz kaç haneden oluşsun? "))

        if n < 8:
            print("Çok kısa! Güvenliğiniz için en az 8 karakter kullanın. ")
        else: 
            karakterler = string.ascii_letters + string.digits + string.punctuation 

            sifre = ""
            for i in range(n):
                sifre += random.choice(karakterler)

            print("Oluşturulan Şifre: ", sifre)

    except ValueError:
        print("HATA!")
