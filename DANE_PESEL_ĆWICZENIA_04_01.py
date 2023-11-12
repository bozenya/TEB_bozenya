data = []


def add_row():
    name_surname = add_name()
    bd = add_pesel()

    data.append({'name': name_surname[0],
                 'surname': name_surname[-1],
                 'pesel': bd[2],
                 'sex': bd[1],
                 'birth_date': bd[0]})


def add_name():
    name_surname = input("Podaj imie i nazwisko: ")
    name_surname = name_surname.split(" ")
    while True:
        for n in range(len(name_surname)):
            if name_surname[n] == "":
                del name_surname[n]
        if (len(name_surname) < 2):
            name_surname.append(input("Podaj brakujące dane (imię/nazwisko): "))
            continue
        break
    for n in range(len(name_surname)):
        name_surname[n] = name_surname[n][0].upper() + name_surname[n][1:].lower()
    return name_surname


def add_pesel():
    pesel = input("Podaj pesel: ")
    while True:
        pesel_sum = 0
        if (len(pesel) == 11):
            wage = 9
            for i in range(len(pesel)):
                wage = 1 if i == 10 else 3 if wage == 1 else 7 if wage == 3 else 9 if wage == 7 else 1
                pesel_sum += int(pesel[i]) * wage
        if str(pesel_sum)[-1] == "0":
            break
        pesel = input("Podaj pesel właściwy:  ")
    sex = 'M' if int(pesel[9]) % 2 == 1 else 'K'
    birth_date = ''
    mprefix = int(pesel[2]) #pobierz trzeci 3. znak z pesela, zmienna
    if mprefix < 2:
        birth_date = '19'
    elif mprefix < 4:
        birth_date = '20'
    elif mprefix < 6:
        birth_date = '21'
    elif mprefix < 8:
        birht_date = '22'
    elif mprefix < 10:
        birth_date = '18'
      #pesel[:2] - pobiera do 2 elementów, czyli indeksy 0,1
    birth_date += pesel[:2] + "-" + str(mprefix % 2) + pesel[3] + "-" + pesel[4:6]
    birth_date = birth_date.split("-")
    birth_dict = {"y": birth_date[0], "m": birth_date[1], "d": birth_date[2]}
    return (birth_dict, sex, pesel)


def pokaz_dane():
    print(data)


def save_file(f='osoby.csv'):
    # r - plit otwarty tylko do odczytu (błąd jeżeli plik nie istnieje)(domyślne)
    # r+ - plik otwarty do odczytu i zapisu (błąd jeżeli plik nie istnieje)
    # w - plik otwarty do zapisu (utworzy plik lub podmieni istniejący)
    # w+ - plik otwarty do zapisu i odczytu (utworzy plik lub podmieni istniejący)
    # a - otwiera istniejący plik do dopisania treści (nie usuwa istniejącej)
    # a+ - otwiera plik do nadpisania i odczytu
    # x - jeżeli plik nie istnieje - tworzy go; jeżeli istnieje to wywołuje błąd

    # t - prefix wskazujący na pracę z plikiem tekstowym (domyślne)
    # b - prefix wskazujący na pracę z plikiem binarnym
    # przykład wykorzystania otwierania plików:
    # open(plik, "tr") - tekstowy do odczytu   open(plik, "r")
    # open(plik, "tw+") plik tekstowy  do zapisu i odczytu open(plik, "w+")
    # open(plik, "br+") plik binarny do odczytu i zapisu
    fd = open(f, "w") #file descriptor
    fd.write("name;surname;pesel;sex;birth_year;birth_month;birth_day\n")
    for d in data:
        fd.write(
            f"{d['name']};{d['surname']};{d['pesel']};{d['sex']};{d['birth_date']['y']};{d['birth_date']['m']};{d['birth_date']['d']}")
        fd.write("\n")
    fd.close() #zamknij plik
def load_file(f = 'osoby.csv'):
    fd = open(f, "r")
    fd.readline()
    while True:
        d = fd.readline().strip()
        if not d:
            break
        d = d.split(";")
        print(d)
        data.append({'name': d[0],
                 'surname': d[1],
                 'pesel': d[2],
                 'sex': d[4],
                 'birth_date': {'y': d[4], 'm': d[5], 'd':[6]}})
while True:
    load_file()
    print("Wybierz opcje:")
    print("1 dodaj")
    print("2 pokaż dane")
    print("3 edycja\n4 zapisz")
    menu = input("Twój wybór:")
    match (menu):
        case "1":
            add_row()
        case "2":
            pokaz_dane()
        # case "3": edit_date()
        case "4":
            save_file()
            break
        case _:
            print("BŁĄD")