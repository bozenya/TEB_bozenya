tajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
liczba = int(input("Podaj liczbę:  "))

while liczba != tajny_numer:
    if liczba > tajny_numer:
        liczba = int(input("Za duża liczba. Podaj liczbę:  "))

    else:
        liczba = int(input("Za mała liczba. Podaj liczbę:  "))
else:
    print("Brawo! Liczba to 777")