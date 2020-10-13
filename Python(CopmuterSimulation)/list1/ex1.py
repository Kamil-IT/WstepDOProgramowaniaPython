import random

import numpy as np
from scipy.stats import gmean, hmean, mode, iqr


def generalized_mean(array, row):
    sum = 0.0
    for number in array:
        sum += number ^ row
    sum = sum / len(array)
    return sum ** (1. / row)


def logarithmic_mean(a, b):
    return (a - b) / (np.log(a) - np.log(b))


randomNumbers = []
for i in range(0, 1000):
    randomNumbers.append(random.randint(1, 1000))
arrayNp = np.array(randomNumbers)

# Info about numbers
print("Random 100 numbers: " + randomNumbers.__str__())
print()

# 1. Avg arithmetic / średnia arytmetyczna
print("Average arithmetic: " + np.mean(arrayNp).__str__())
print()

# 2. Avg geometric / średnia geometryczna
print("Average geometric: " + gmean(randomNumbers).__str__())
print()

# 3. Generalized mean / średnia potęgowa
print("Generalized mean: " + generalized_mean(randomNumbers, 3).__str__())
print()

# 4. Harmean / średnia harmoniczna
print("Harmean: " + hmean(randomNumbers).__str__())
print()

# 5. Logarithmic mean / średnia logarytmiczna
print("Logarithmic mean: " + logarithmic_mean(randomNumbers[0], randomNumbers[1]).__str__())
print()

# 6. Standard deviation / odchylenie standardowe
print("Standard deviation: " + np.std(arrayNp).__str__())
print()

# 7. Variance / wariancja
print("Variance: " + np.var(arrayNp).__str__())
print()

# 8. Mode / dominanta
print("Mode: " + mode(randomNumbers).__str__())
print()

# 9. First quartile / pierwszy kwartyl
print("First quartile: " + np.quantile(arrayNp, 0.25).__str__())
print()

# 10. Second quartile / drugi kwartyl
print("Second quartile: " + np.quantile(arrayNp, 0.5).__str__())
print()

# 11. Third quartile / trzeci kwartyl
print("Third quartile: " + np.quantile(arrayNp, 0.75).__str__())
print()

# 12. Interquartile range / rozstęp ćwiartkowy
print("Interquartile range: " + iqr(randomNumbers).__str__())
print()
