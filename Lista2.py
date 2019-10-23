# zadanie 1
# Określniki formatu

print("Jan %s -- uzyto typu string" % "Nowak")
print("Liczba dni w roku %d -- uzyto liczby calkowitej" % 365)
print("Pi ma wartosc ~%f -- uzyto zmiennoprzcinkowej liczby" % 3.1415926)
print("Odleglosc ziemi od słonca: %Ekm --uzyto duzej liczby w notacji wykładniczej" %149600000)
print("Odleglosc ziemi od słonca: %.02fkm --uzyto duzej liczby w kontrolowanej notacji wykładniczej" %149600000)



# zadanie 2
zmiennaTypuLiczbowego = 10
zmiennaTypuZnakowego = str(zmiennaTypuLiczbowego)
zmiennaTypuLiczbowegoKonwersja = int(zmiennaTypuZnakowego)

print(zmiennaTypuZnakowego, zmiennaTypuLiczbowego, zmiennaTypuLiczbowegoKonwersja)

# zadnie 3

zmiennaDodawana = 2+2
print(zmiennaDodawana)

# zadanie 4

listaKrajow = ["Hiszpania", "Anglia", "Nowa Zelandia", "Niemcy", "USA", "Australia", "Austria", "Japonia", "Czechy"]
listaKrajow += ["Barcelona", "Londyn", "Alla", "Berlin", "Nowy Jork", "AustlialickieMiasto", "AusMiasto", "JaponMiasto", "Praga"]




print(listaKrajow[0] + " " + listaKrajow[9])
print(listaKrajow[1] + " " + listaKrajow[10])
print(listaKrajow[2] + " " + listaKrajow[11])
print(listaKrajow[3] + " " + listaKrajow[12])
print(listaKrajow[4] + " " + listaKrajow[13])
print(listaKrajow[5] + " " + listaKrajow[14])
print(listaKrajow[6] + " " + listaKrajow[15])
print(listaKrajow[7] + " " + listaKrajow[16])
print(listaKrajow[8] + " " + listaKrajow[17])


print("Dlugosc listy to: ")
print(len(listaKrajow))
