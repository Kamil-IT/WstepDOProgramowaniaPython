import math

# Zadanie 1
# A = int(input("Podaj A: "))
# B = int(input("Podaj B: "))
# C = int(input("Podaj C: "))

A = 1
B = 2
C = 1

delta = pow(B, 2) - (4 * A * C)

if delta > 0:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)
    print("Rownanie x^2*" + str(A) + " + x*" + str(B) + " + " + str(C) + "  ma dwa roziązania: x1= " + str(
        x1) + " x2= " + str(x2))
elif delta == 0:
    x1 = (-B - math.sqrt(delta)) / (2 * A)
    print("Rownanie x^2*" + str(A) + " + x*" + str(B) + " + " + str(C) + "  ma jedno roziązanie: x= " + str(x1))
else:
    print("To rownanie nie ma rozwiązań")

# Zadanie 2

silnia = 1
for i in range(1, 5):
    silnia *= i

print(silnia)

# Zadanie 3

N = int(input("Ile chcesz podac liczb? : "))
suma = 0
for i in range(1, N + 1):
    suma += int(input("Liczba " + str(i) + " to : "))

srednia = suma / N
print("Średnia uzytkownika  to : " + str(srednia))
if srednia % 2 == 0:
    print("Jest to liczba parzysta")
else:
    print("Jest to liczba nieparzysta")

# zadanie 4

liczbaA = 12
liczbaB = 4

# Najmniejszy wspolny dzielnik
dzielnik = 1
czyZnaleziony = True
while czyZnaleziony:
    dzielnik += 1
    if liczbaA % dzielnik == 0 and liczbaB % dzielnik == 0:
        czyZnaleziony = False

print(dzielnik)
