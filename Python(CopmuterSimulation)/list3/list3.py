import numpy as np
from numpy import genfromtxt
from scipy.stats import ranksums, f_oneway, brunnermunzel, levene, shapiro, kruskal, bartlett, mannwhitneyu, t, nct


def import_list_from_data_cvs(csv_data, column):
    list_ = []
    for i in range(int(csv_data.size / 2)):
        list_.append(csv_data[i][column])
    return list_


data_csv1 = genfromtxt('1.csv', delimiter=',')
data_csv2 = genfromtxt('2.csv', delimiter=',')

col_1_csv1 = import_list_from_data_cvs(data_csv1, 0)
col_2_csv1 = import_list_from_data_cvs(data_csv1, 1)
col_1_csv2 = import_list_from_data_cvs(data_csv2, 0)
col_2_csv2 = import_list_from_data_cvs(data_csv2, 1)

print("Info values")
print(f"col_1_csv1 size:{len(col_1_csv1)}")
print(f"col_2_csv1 size:{len(col_2_csv1)}")
print(f"col_1_csv2 size:{len(col_1_csv2)}")
print(f"col_2_csv2 size:{len(col_2_csv2)}")

# Ranksums
print("Ranksums")
print("csv 1: " + str(ranksums(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(ranksums(col_1_csv2, col_2_csv2)))

# ANOVA
print("ANOVA")
print("csv 1: " + str(f_oneway(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(f_oneway(col_1_csv2, col_2_csv2)))

# Brunner-Munzel
print("Brunner-Munzel")
print("csv 1: " + str(brunnermunzel(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(brunnermunzel(col_1_csv2, col_2_csv2)))

# Levene
print("Levene")
print("csv 1: " + str(levene(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(levene(col_1_csv2, col_2_csv2)))

# Shapiro-Wilk
print("Shapiro-Wilk")
print("csv 1 col 1: " + str(shapiro(col_1_csv1)))
print("csv 1 col 2: " + str(shapiro(col_2_csv1)))
print("csv 2 col 1: " + str(shapiro(col_1_csv2)))
print("csv 2 col 2: " + str(shapiro(col_2_csv1)))

# Kruskal-Wallis
print("Kruskal-Wallis")
print("csv 1: " + str(kruskal(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(kruskal(col_1_csv2, col_2_csv2)))

# Bartlett
print("Bartlett")
print("csv 1: " + str(bartlett(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(bartlett(col_1_csv2, col_2_csv2)))

# Mann-Whitney
print("Mann-Whitney")
print("csv 1: " + str(mannwhitneyu(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(mannwhitneyu(col_1_csv2, col_2_csv2)))

# t-Student  TODO:
print("t-Student")
# print("csv 1: " + f"T-StudentResult(statistic={t.pdf(1-len(col_1_csv1), col_1_csv1)}, pvalue=")
# print("csv 2: " + str(mannwhitneyu(col_1_csv2, col_2_csv2)))
# Lilliefors TODO:
