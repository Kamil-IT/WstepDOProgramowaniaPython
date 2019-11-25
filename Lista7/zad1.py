import os
import sys
import time

from pip._vendor.distlib.compat import raw_input

import Lista7.DiaryCard

path = "pamietnik.txt"
try:
    data_file = open(path, "a+")
except IOError:
    print("Blad odczytu: " + path)
    sys.exit(0)

# Dane są oddzielane ";"
# WARNING NIE wprwadzaj do swojego pamiętnika ; !!!!

diary = []

if os.path.getsize(path) > 0:
    line = data_file.readline()
    while line != '':
        if line in ';':
            title = line[:line.find(';')]
            text = line[line.find(';')]
        else:
            continue

        diary += [Lista7.DiaryCard]

print("Obecny pamietnik:")
# for pamietnik in Nie moge odwołać się do metod
# for tmp in diary:
#     print("title: " + tmp.)
#     print(tmp)



title = raw_input("Wprowadz tytul: ")
text = raw_input("Wprowadz wartosc tekstowa pamietnika: ")

data_file.write(title + ";" + text + ";" + time.ctime(time.time()) + "\n")
data_file.write(title + ";" + text + "\n")


