import random


class Liczba_losowa:
    def losuj01(self):
        return random.random()

    def losuj_liczbe(self, x, y):
        return random.randint(x, y)


liczba_losowa = Liczba_losowa()

print(Liczba_losowa.losuj01(liczba_losowa))

print(Liczba_losowa.losuj_liczbe(liczba_losowa, 1, 10))
