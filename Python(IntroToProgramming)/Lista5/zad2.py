from typing import Type


class Student:

    def __init__(self, imie, nazwisko, rok, grupa, nrAlbumu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok
        self.grupa = grupa
        self.nrAlbumu = nrAlbumu

    def change_date(self, grupa, rok):
        self.grupa = grupa
        self.rok = rok


student = Student("Marcin", "Kowalski", 1990, "Nieznana", 254331)
