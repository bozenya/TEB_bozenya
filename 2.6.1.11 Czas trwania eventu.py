
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

    k = int(y/60)   #tworzy zmienną k co mi doda godziny

    h += k          #powiększa format godziny o zmienną k

    m = y - (k*60)  #minuty startowe ustawia przez k przeobrażoną na minuty

if h >= 24:         #gdy (dodawany już) czas jest większy od 24

    zmienna = (24 * int((d/60)/24)) #tworzy zmienną, która sprawdza czy czas wydarzenia nie jest 0 i wylicza godzinę do odjęcia (??? nie wiem co tu zaszło)

    if zmienna == 0:                #gdy zmienna to 0

        zmienna = int(d/60)         #???

        h -=24                      #odejmuje z formatu godzin (np. 25,30) liczbę 24 i nadaje własciwy format h

    else:
        h -= zmienna                #odejmuje godziny stworzone przez zmienną = (24 * int((d/60)/24))

print(h,":", m)                     #przedstawia czas zakończenia np. 20:45

