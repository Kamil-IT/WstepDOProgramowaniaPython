import numpy.random as rnd
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

n = 500
x1 = 4 * rnd.rand(n) - 3
y1 = 4 * rnd.rand(n) - 3
z1 = 4 * rnd.rand(n) - 3

x2 = 4 * rnd.rand(n) + 10
y2 = 4 * rnd.rand(n)
z2 = 4 * rnd.rand(n)

x3 = 0
y3 = 0
z3 = 5

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(x1, y1, z1)
ax.scatter(x2, y2, z2)
ax.scatter(x3, y3, z3, 'y')

data_blue = pd.DataFrame([[x1[i], y1[i], z1[i]] for i in range(len(x1))])
data_yellow = pd.DataFrame([[x1[i], y1[i], z1[i]] for i in range(len(x1))])



pca = PCA()

pca.fit(data_blue)

print(pca.explained_variance_)
print(pca.components_)


plt.show()



# Metoda pca ograniczenia wymiarów
# Klasyfikatory implementacja prosycha metod klasyfikacji np. k_najblirzych sasiadów
# Klasyfikator
# SVN drzewa decyzyjne i sieci neuronowe
# metody klasyfikacji to z dzisiaj
# Generacja zbiorów syntetyczny zbiór z ilościa klas