# zadanie 1
# Określniki formatu

print("Jan %s -- uzyto typu string" % "Nowak")
liczba = 365+10
print("Liczba dni w roku %d -- uzyto liczby calkowitej" % liczba)
y = 3.1415926 * 1.3
print("Pi ma wartosc ~%f -- uzyto zmiennoprzcinkowej liczby" % y
      )
y = 149600000 / 1000
print("Odleglosc ziemi od słonca: %Ekm --uzyto duzej liczby w notacji wykładniczej" % y
      )
d = 149600000 % 35
print("Odleglosc ziemi od słonca: %.02fkm --uzyto duzej liczby w kontrolowanej notacji wykładniczej" % d
      )



# zadanie 2
zmiennaTypuLiczbowego = 10
zmiennaTypuZnakowego = str(zmiennaTypuLiczbowego)
zmiennaTypuLiczbowegoKonwersja = int(zmiennaTypuZnakowego)

print(zmiennaTypuZnakowego, zmiennaTypuLiczbowego, zmiennaTypuLiczbowegoKonwersja)

# zadnie 3


liczba = 10
zmiennaDodawana = 2
zmiennaDodawana %= liczba
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
