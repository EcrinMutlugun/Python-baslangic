import random
sayi = random.randint(1,100)
sayac = 0
while True :
    try :
        tahmin = int(input("Tahmin: "))
        sayac += 1
        if tahmin < sayi :
            print("Daha büyük sayı gir. ")
        elif tahmin > sayi :
            print("Daha küçük sayı gir. ")
        else :
            print(f"Tebrikler, {sayac} denemede bildin! ")
            break
    except ValueError :
        print("Lütfen yalnızca sayı gir! ")