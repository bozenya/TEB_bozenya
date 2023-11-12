#LISTA

imiona = ["Krysia", "Adam", "Pola", "Marta"]
wiek = [20, 8, 67, 45]

#for imie in imiona:
   # print("Imie:", imie, "Wiek:", wiek)

for index in range(len(imiona)):
    print(imiona[index], wiek[index])
print("-----------------------------")
daty = []
prz = True
while prz: #prz zamist True
    zm = input("Podaj date:")
    if zm == '':
        prz = False
        continue
    daty.append(zm)
    print(daty)
else:
    print(daty)
print("-----------------------------")

#KROTKA

imiona = ("Krysia", "Adam", "Pola", "Marta")
wiek = (20, 8, 67, 45)

for imie in imiona:
   print(imiona)

print("-----------------------------")

#ZBIÓR

imiona = {"Krysia", "Adam", "Pola", "Marta"}
wiek = {20, 8, 67, 45}

imiona.add(input("Dodaj imie: "))
print(imiona)
imiona.remove("Adam")
print(imiona)

print("-----------------------------")

#SŁOWNIK

imiona = {'baby':["Krysia", "Pola", "Marta"]}
print(imiona['baby'])