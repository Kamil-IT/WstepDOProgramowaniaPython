import os
import sys

path = "pamietnik.txt"
try:
    data_file = open(path, "a+")
except IOError:
    print("Blad odczytu: " + path)
    sys.exit(0)

# Dane są oddzielane ";"
# WARNING NIE wprwadzaj do swojego pamiętnika ; !!!!

pamietnik = {}

if os.path.getsize(path) > 0:
    line = data_file.readline()
    while line != '':
        if line in ';':
            title = line[:line.find(';')]
            text = line[line.find(';')]
        else:
            continue
        pamietnik[title] = [text]

print("Obecny pamietnik:")
# for pamietnik in


title = input("Wprowadz tytul: ")
text = input("Wprowadz wartosc tekstowa pamietnika: ")

data_file.write("\n" + title + ";" + text + "\n")
