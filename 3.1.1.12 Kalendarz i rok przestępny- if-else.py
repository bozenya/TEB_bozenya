rok = int(input("Wprowadź rok: "))
if rok >= 1582:
    if rok % 4 != 0:
        print("Rok zwykły")
    elif rok % 100 != 0:
        print("Rok przestępny")
    elif rok % 400 != 0:
        print("Rok zwykły")
    else:
        print("Rok przestępny")
else:
    print("Nie w kalendarzu gregoriańskim")