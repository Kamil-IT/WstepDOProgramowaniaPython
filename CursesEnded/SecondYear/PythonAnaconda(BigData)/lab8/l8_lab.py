# Link https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones

# Generacja
# Filtracja
# Sortowanie od naważniejsej cechy do najmniej ważne   (metoda pca)

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

# cel pojektu
# opisać narzędzia
# Napisać jak to zostało rozwiązane
# Opisać wyniki
# Tabelki / Wykresy
# Przeprowadzić analizę np. stosujac taki i taki alorytm to to i to a taki to to i to
# Czas do 15.06
#

# Na kolosie PCA i LDA ranking cech
df = pd.read_csv('dataset/test/X_test.txt', header=None, delimiter=r"\s+")

pca = PCA()

pca.fit(df)

print(pca.explained_variance_)
print(pca.components_)