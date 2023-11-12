
wys = 0
blokow = int(input("Wprowadź liczbę bloków: "))
bloki_uzyte = 0
krok = 1

while blokow > bloki_uzyte:
    bloki_uzyte += krok
    if bloki_uzyte > blokow:
        break
    else:
        wys += 1
        krok +=1
        print(wys)
print("Wysokość piramidy wynosi:", wys)
