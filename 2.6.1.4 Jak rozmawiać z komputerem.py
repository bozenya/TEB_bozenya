cokolwiek = int(input("Wpisz liczbe: "))
cos = cokolwiek ** 2.0
print(cokolwiek, "do potegi 2 wynosi", cos)

#rysuje prostokąt
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

bok_a = float(input("Wprowadz dlugosc pierwszego boku: "))
bok_b = float(input("Wprowadz dlugosc drugiego boku: "))
print("Dlugosc przeciwprostokatnej wynosi " + str((bok_a**2 + bok_b**2)))