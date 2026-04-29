def faktoriyel_for(sayi):
    fakt =1
    i=1
    for i in range(1,sayi+1):
        fakt *= i
        i += 1
    return fakt


def faktoriyel_while(sayi):
    i = 2
    fakt =1
    while i <= sayi:
        fakt *= i
        i+=1
    return fakt


while True:
        try:
            sayi = int(input("Lütfen bir sayı giriniz: "))
        except ValueError:
            print("Lütfen yalnızca sayı girin! ")
            continue

        print(f"For döngüsü: ", faktoriyel_for(sayi))
        print(f"While döngüsü: ", faktoriyel_while(sayi))
