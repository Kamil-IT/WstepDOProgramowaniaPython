import sys
import time
from pip._vendor.distlib.compat import raw_input
from Lista7.DiaryCard import DiaryCard

path = "pamietnik.txt"
try:
    data_file = open(path, "r")
except IOError:
    print("Blad odczytu: " + path)
    sys.exit(0)

# Dane są oddzielane ";"
# WARNING NIE wprwadzaj do swojego pamiętnika ; !!!!

diary = []
lines = data_file.readlines()

for tmp in lines:
    title = tmp[:tmp.find(';')]
    text = tmp[tmp.find(';')+1:tmp.find(';', tmp.index(';') + 1)]
    date = tmp[len(title) + len(text)+2:]
    diary += [DiaryCard(title, text, date)]


data_file.close()


print("Obecny pamietnik od przodu:")
for tmp in diary:
    print("title: " + tmp.title + "     Date: " + tmp.date, end='')
    print(tmp.text)
    print()

print("Obecny pamietnik od tylu:")
for x in range(len(diary)-1, -1, -1):
    print("title: " + diary[x].title + "     Date: " + diary[x].date, end='')
    print(diary[x].text)
    print()
title = raw_input("Wprowadz tytul: ")
text = raw_input("Wprowadz wartosc tekstowa pamietnika: ")

data_file = open(path, "a")
data_file.write(title + ";" + text + ";" + time.ctime(time.time()) + "\n")
data_file.close()
