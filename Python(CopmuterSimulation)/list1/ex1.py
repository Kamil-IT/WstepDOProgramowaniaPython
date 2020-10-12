import random
import numpy as np
from scipy.stats import gmean
from scipy.stats import hmean
from scipy.stats import mode
from scipy.stats import iqr

randomNumbers = []
for i in range(0, 1000):
    randomNumbers.append(random.randint(1, 1000))
arrayNp = np.array(randomNumbers)

# Info about numbers
print(randomNumbers)

# 1. Avg arithmetic / średnia arytmetyczna
print("Average arithmetic: " + np.average(arrayNp))
print()

# 2. Avg geometric / średnia geometryczna
print("Average geometric: " + gmean(randomNumbers))
print()

# 3. Generalized mean / średnia potęgowa
# TODO
print("Generalized mean: ")
print()

# 4. Harmean / średnia harmoniczna
print("Harmean: " + hmean(randomNumbers))
print()

# 5. Logarithmic mean / średnia logarytmiczna
# TODO:
print("Logarithmic mean: ")
print()

# 6. Standard deviation / odchylenie standardowe
print("Standard deviation: " + np.std(arrayNp))
print()

# 7. Variance / wariancja
print("Variance: " + np.var(arrayNp))
print()

# 8. Mode / dominanta
# TODO: might be error
print("Mode: " + mode(randomNumbers).__str__())
print()

# 9. First quartile / pierwszy kwartyl
# TODO: https://numpy.org/doc/stable/reference/generated/numpy.quantile.html
print("First quartile: ")
print()

# 10. Second quartile / drugi kwartyl
# TODO: https://numpy.org/doc/stable/reference/generated/numpy.quantile.html
print("Second quartile: ")
print()

# 11. Third quartile / trzeci kwartyl
# TODO: https://numpy.org/doc/stable/reference/generated/numpy.quantile.html
print("Third quartile: ")
print()

# 12. Interquartile range / rozstęp ćwiartkowy
print("Interquartile range: " + iqr(randomNumbers))
print()


