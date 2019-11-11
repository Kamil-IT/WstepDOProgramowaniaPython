import datetime

from github.WstepDoProgramowania.Lista6.zad2.countDate import cont_after_1800


print(datetime.datetime(2000, 5, 5) - datetime.datetime(2000, 5, 4))

day1 = int(input("Dzien: "))
month1 = int(input("Miesiac: "))
year1 = int(input("Rok "))
day2 = int(input("Dzien: "))
month2 = int(input("Miesiac: "))
year2 = int(input("Rok "))



print(cont_after_1800(datetime.datetime(year1, month1, day1), datetime.datetime(year2, month2, day2)))

