import datetime

kartonMleka = {
    "waznosc_mleka" : datetime.datetime(2020, 5, 17),
    "waga" : 10.0,
    "koszt" : 25.0,
    "marka" : "Laciate"
}

keysList = list(kartonMleka.keys())

print(kartonMleka["waznosc_mleka"], kartonMleka["koszt"], kartonMleka["marka"], kartonMleka["koszt"], kartonMleka["waga"])
print(kartonMleka.items())


