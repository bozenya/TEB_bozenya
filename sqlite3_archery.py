import sqlite3

def print_hi(name):
  print(f'Hi, {name}')


if __name__ == '__main__':
  print_hi('PyCharm')


def printAll():
    data = selectAll()
    if len(data) > 0:
        for i in data:
            print(i)
    else:
        print("Brak danych")

def printData(data):
    if len(data) > 0:
        for i in data:
            print(i)
    else:
        print("Brak danych")
def selectAll():
    query_request = "SELECT * FROM luki;";
    #where = "WHERE " + col + "=?;"
    mycursor.execute(query_request) # + where, (txt,))
    #print(query_request)
    data = mycursor.fetchall()
    return data

def selectWhere(txt):
    query_request = "SELECT * FROM luki WHERE ID_łuk like '%" + txt + "%' or ID_uzbrojenie like '%" + txt + "%' or rodzaj like '%" + txt + "%' or producent like '%" + txt + "%' or dostępność like '%" + txt + "%';";
    #where = "WHERE " + col + "=?;"
    mycursor.execute(query_request) # + where, (txt,))
    print(query_request)
    data = mycursor.fetchall()
    return data

def selectWhereID(txt):
    query_request = "SELECT * FROM luki WHERE ID_łuk = '" + txt +  "';";
    #where = "WHERE " + col + "=?;"
    mycursor.execute(query_request) # + where, (txt,))
    print(query_request)
    data = mycursor.fetchall()
    return data

def updateLuki(ID_łuk, koszt, numer_lokalizacji, dostępność, mydb):
    data = selectWhereID(ID_łuk)
    if koszt == '' or data[0][7] == koszt:#weryfikuj
        koszt = str(data[0][7])
    if numer_lokalizacji == '' or data[0][8] == numer_lokalizacji:
        numer_lokalizacji = str(data[0][8])
    if dostępność == '' or data[0][9] == dostępność:
        dostępność = str(data[0][9])

    query_request = "UPDATE luki SET 'koszt' = '" + koszt + "', 'numer_lokalizacji' = '" +numer_lokalizacji+ "', 'dostępność' = '" +dostępność+ "' WHERE ID_łuk='"+ID_łuk+"';"
    print(query_request)
    mycursor.execute(query_request)
    mydb.commit()

def insertLuki(ID_właściwości, ID_uzbrojenie, rodzaj, producent, model, lata_gwarancji, koszt, numer_lokalizacji, dostępność, opis, opinie, mydb):
    query_request = "INSERT INTO luki VALUES (null, '"+ str(ID_właściwości) +"', '"+ str(ID_uzbrojenie) +"', '"+ rodzaj +"', '"+ producent +"', '"+ model +"', '"+ str(lata_gwarancji) +"', '"+ str(koszt) +"', '"+ numer_lokalizacji +"', '"+ dostępność +"', '"+ opis +"', '"+ opinie +"');"
    mycursor.execute(query_request)
    print(query_request)
    mydb.commit()

def deleteLukiID(ID_łuk, mydb):
    query_request = "DELETE FROM luki where ID_łuk =  '"+ str(ID_łuk) +"';"
    mycursor.execute(query_request)
    print(query_request)
    mydb.commit()

def deleteLukiModel(model, mydb):
    query_request = "DELETE FROM luki where model =  '"+ model +"';"
    mycursor.execute(query_request)
    print(query_request)
    mydb.commit()

# Tworzenie połączenia z bazą danych
mydb = sqlite3.connect('db.sqlite3')

# Tworzenie kursora
mycursor = mydb.cursor()


# Pobieranie danych
print("---------- ALL ----------------------------------")

printAll()

print("---------- WHERE  -  FILTRUJ PO KOLUMNIE ----------------------------------")

data = selectWhere("Bloczkowe") #wpisz Bloczkowe pokaże wszystko Bloczkowe, unikalne wyszukiwanie

printData(data)

print("---------- WHERE  -  FILTRUJ PO ID ----------------------------------")

data = selectWhereID("2")

printData(data)

print("---------- UPDATE ----------------------------------")

data = updateLuki('13','209','55',str(1), mydb)

printAll()

print("---------- INSERT ----------------------------------")

#data = insertLuki(71, None, 'Klasyczne', 'Rolan', 'Snake', 5, 209, '12', str(1), 'to idealny łuk na imprezy integracyjne, obozy dla młodzieży, dla ośrodków wypoczynkowych oraz dla rodzin, czy dzieci lub młodzieży, którzy zaczynają się interesować łucznictwem.', mydb)

printAll()

print("---------- DELETE ----------------------------------")

#data = deleteLukiID(9, mydb)
#printAll()

#deleteLukiModel('Galeon', mydb)
#printAll()
# Zamykanie połączenia
mydb.close()


