
"""
h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

koniec_h = ((h*60+m)+d)//60
koniec_m = ((d/60) % 60)

print(koniec_h, ":", koniec_m)

print(4/11)
"""

h = int(input("Czas startu (godziny): "))

m = int(input("Czas startu (minuty): "))

d = int(input("Czas trwania wydarzenia (minuty): "))

x = int((m+d)/60) #ilosc godzin ktore dodaje uzytkownik

y = (m+d)  #ilosc minut ktore dodaje uzytkownik

if y > 60:          #gdy minuty eventu przekroczą 60 (min zegarowych)

    k = int(y/60)   #tworzę zmienną k co mi doda godziny

    h += k          #powiększam format godziny o zmienną k

    m = y - (k*60)  #

if h >= 24:

    zmienna = (24 * int((d/60)/24))

    if zmienna == 0:

        zmienna = int(d/60)

        h -=24

    else:

        h -= zmienna

print(h,":", m)