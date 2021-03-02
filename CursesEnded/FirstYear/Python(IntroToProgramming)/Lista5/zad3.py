import random


class NormalnyGenerator:
    NORMALNY_GENERATOR_LOSOWY = 1

    def losujNaturalne(self, x, y):
        return random.randint(x, y)


class WykladniczyGenerator:
    WYKLADNICZY_GENERATOR_LOSOWY = 2


    def losujWykladniczo(self, x, y):
        return random.random()*float(random.randint(x, y))


class Liczba_losowa(NormalnyGenerator, WykladniczyGenerator):
     def __int__(self):
         self.losuj01(self)

     def losuj01(self):
        return random.random()

     def losuj_liczbe(self, generator_losowy, x, y):
        if generator_losowy == NormalnyGenerator.NORMALNY_GENERATOR_LOSOWY:
            return self.losujNaturalne(x, y)
        if generator_losowy == Liczba_losowa.WYKLADNICZY_GENERATOR_LOSOWY:
            return self.losujWykladniczo(x, y)


liczba_losowa = Liczba_losowa()

print(Liczba_losowa.losuj01(liczba_losowa))

print(Liczba_losowa.losuj_liczbe(liczba_losowa, Liczba_losowa.NORMALNY_GENERATOR_LOSOWY, 1, 5))
print(Liczba_losowa.losuj_liczbe(liczba_losowa, Liczba_losowa.WYKLADNICZY_GENERATOR_LOSOWY, 1, 5))
