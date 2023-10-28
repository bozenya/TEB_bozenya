dochod = float(input("Wprowadź swój roczny dochód: "))

if dochod <= 85528:
    podatek = 0.18 * dochod - 556.2
    if podatek < 0:
        podatek = 0
else:
    podatek = 14839.02 + (dochod - 85528)*0.32

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)