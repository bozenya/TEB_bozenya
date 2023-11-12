slowo = input("Podaj słowo: ")
slowo = slowo.upper()
slowo2 = ""
for i in range(len(slowo)):
    if i == "E" and i == "I" and i == "O" and i == "U" and i == "A":
        slowo2 -= slowo[i]
        print(slowo2)
    else:
        #slowo2 += slowo[i]
        print(slowo2)



      #  slowo_nowe = slowo.replace(str(i), str(""))
       # print(slowo.replace(str(i), ""))
        #print(slowo_nowe)