dates = []

def sprawdz_separator(data):
    cyfry = tuple([f'{x}' for x in range(10)]) #generacja liczb w krotce tuple, skrócony zapis
    #print(cyfry)
    for znak in data:
        if znak in cyfry:
            continue
        return znak
def sep_date(date, separator = '.'): #SEPARATOR DATY
    data = date.split(separator)
    if separator == '/':
        data[0], data[1] = data[1], data[0] #zamiana mies na dni system US
    return data


def czy_przestepny(rok):
    #operator trójstanowy działanie:
    #polecenie (kod_jeżeli_prawda) if <warunek> else (kod_jeżeli_fałsz)
    #return True if rok % 4 == 0 .. else False
    return True if ((rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0) else False
    #pass - wyjdź
    #return- geneza słowa: procesor wypluwa
def czy_prawidlowe_dni(dni, miesiac, przestepny):
    print(dni, miesiac, przestepny)
    if dni <= 0 or dni > 31:
        return False
    if miesiac == 0 or miesiac >= 12:
        return False
    if miesiac == 2 and przestepny and dni <= 29:
        return True
    if miesiac == 2 and dni <= 28:
        return True
    if miesiac == 2:
        return False
    if miesiac >= 1 and miesiac <=7 and miesiac % 2 ==1 and dni > 0 and dni <= 31:
        return True
    if miesiac >=8 and miesiac <=12 and miesiac % 2 ==0 and dni > 0 and dni <= 30:
        return True
    if dni <= 30:
        return True
    return False

def get_dict_from_value(value, key, dict_list):
    for s in dict_list:
        if s[key] == value:
            return s
    return None
def sortuj(kryt=2):
    zwrot = []
    klucz = 'year' if kryt==2 else 'month' if kryt==1 else 'day' #oper.trójstanowy if else
    klucze = []
    for s in dates:
        klucze.append(int(s[klucz]))#zapisuje wszystkie klucze
    klucze.sort() #sort zastapi to co powyzej
    #print(klucze)
    for i in range(len(dates)):
        zwrot.append(get_dict_from_value(str(klucze[i]), klucz, dates))
    return zwrot

    """i = 1
        while i<len(klucze):
            if klucze[i] < klucze [i-1]:
                klucze[i], klucze [i-1] = klucze[i-1], klucze [i]
                i = 1
                continue
            i+=1"""


def wyswietl_chrono():
    kryt = input("Podaj priorytet sortowania (dzień (0), miesiąc (1) , ROK (2)): ")
    kryt = kryt.lower()
    if (kryt == '' or kryt[0] in ('r', 'y', '2')):
        kryt = 2
    elif (kryt[0] in ('d', '0')):
        kryt = 0
    elif (kryt[0] in ('m', '1')):
        kryt = 1
    else:
        return
    print_all(sortuj(kryt))
def add_date():
    global dates
    date = input("Podaj date do zapisania:")
    if date == '':
        print('Data pusta nie dodaje')
        return
    date_array = sep_date(date, sprawdz_separator(date))

    #czy data jest poprawna?
    #czy rok jest przestępny?
    if czy_prawidlowe_dni(int(date_array[0]), int(date_array[1]), czy_przestepny(int(date_array[2]))):
        dates.append({'day': date_array[0],
                      'month':date_array[1],
                      'year':date_array[2],
                      'us': True if sprawdz_separator(date) == '/' else False})
        print('Data prawidłowa')
    else:
        print('Data zła')


def print_all(in_list=dates):
    index = 1
    for s in in_list:
        str_ret = ""
        if s["us"]:
            str_ret += s["month"] + "/" + s["day"] + "/"
        else:
            str_ret += s["day"] + "." + s["month"] + "."
        str_ret += s["year"]
        print(index, str_ret)
        index += 1


def remove_date():
    global dates
    print_all()
    d = int(input("Podaj date do usuniecia:"))
    dates.remove(date[d])

while True:
    print("Witaj w słowniku. Wybierz opcje:")
    print("1 dodaj:")
    print("2 wyswietl:")
    print("3 usuń:\n4 zakończ")
    menu = input("Twój wybór:")
    match(menu):
        case "1": add_date()
        case "2": wyswietl_chrono()
        case "3": remove_date()
        case "4": break
        case _: print("BŁĄD")

"""
match(kryt):
        case 'dzień': print(sortuj(0))
        case 'miesiąc': print(sortuj(1))
        case 'rok': print(sortuj())
        case _: print("BŁĄD")


while True:
    date = input("Podaj date do zapisania:")
    if date == '':
        break
    date_array = sep_date(date, sprawdz_separator(date))

    #czy data jest poprawna?
    #czy rok jest przestępny?
    if czy_prawidlowe_dni(int(date_array[0]), int(date_array[1]), czy_przestepny(int(date_array[2]))):
        dates.append({'day': date_array[0],
                      'month':date_array[1],
                      'year':date_array[2],
                      'us': True if sprawdz_separator(date) == '/' else False})
        print('Data prawidłowa')
    else:
        print('Data zła')

    if czy_przestepny(int(date_array[2]) if len(date_array[2]) == 4 else int('20' + date_array[2])):
        print(date_array, 'Przestępny')

    else:
        print(date_array, 'Nieprzestępny')
"""

    # F if nieprzestepny i T jezeli przestepny
