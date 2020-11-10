from collections import namedtuple

import numpy as np
from numpy import genfromtxt
from scipy.stats import ranksums, f_oneway, brunnermunzel, levene, shapiro, kruskal, bartlett, mannwhitneyu, t, nct, \
    norm, normaltest, ttest_ind
from statsmodels.stats._lilliefors import lilliefors


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

# Parametryczne -> rozkład normalny
# nie Parametryczne -> nie rozkład normalny

print("Info values")

print(f"csv1 size:{len(col_1_csv1)}, normal: {False}")
print(f"csv2 size:{len(col_1_csv2)}, normal: {True}")

# Shapiro-Wilk - is normal
print("Shapiro-Wilk")
print("csv 1 col 1: " + str(shapiro(col_1_csv1)))
print("csv 1 col 2: " + str(shapiro(col_2_csv1)))
print("csv 2 col 1: " + str(shapiro(col_1_csv2)))
print("csv 2 col 2: " + str(shapiro(col_2_csv1)))

# Lilliefors - is normal
print("Lilliefors")
stat, p_val = lilliefors(col_1_csv1)
print("csv 1, col 1: " + f"LillieforsResult(statistic={stat}, pvalue={p_val})")
stat, p_val = lilliefors(col_2_csv1)
print("csv 1, col 2: " + f"LillieforsResult(statistic={stat}, pvalue={p_val})")
stat, p_val = lilliefors(col_1_csv2)
print("csv 2, col 1: " + f"LillieforsResult(statistic={stat}, pvalue={p_val})")
stat, p_val = lilliefors(col_2_csv2)
print("csv 2, col 2: " + f"LillieforsResult(statistic={stat}, pvalue={p_val})")

# Levene - equality of variances
print("Levene")
print("csv 1: " + str(levene(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(levene(col_1_csv2, col_2_csv2)))

# Ranksums - nonparametric test
print("Ranksums")
print("csv 1: " + str(ranksums(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(ranksums(col_1_csv2, col_2_csv2)))

# Brunner-Munzel - nonparametric
print("Brunner-Munzel")
print("csv 1: " + str(brunnermunzel(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(brunnermunzel(col_1_csv2, col_2_csv2)))

# Kruskal-Wallis - non-parametric
print("Kruskal-Wallis")
print("csv 1: " + str(kruskal(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(kruskal(col_1_csv2, col_2_csv2)))

# Bartlett - non-parametric
print("Bartlett")
print("csv 1: " + str(bartlett(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(bartlett(col_1_csv2, col_2_csv2)))

# Mann-Whitney - non-parametric
print("Mann-Whitney")
print("csv 1: " + str(mannwhitneyu(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(mannwhitneyu(col_1_csv2, col_2_csv2)))

# ANOVA - parametric
print("ANOVA")
print("csv 1: " + str(f_oneway(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(f_oneway(col_1_csv2, col_2_csv2)))

# t-Student
print("t-Student")
print("csv 1: " + str(ttest_ind(col_1_csv1, col_2_csv1)))
print("csv 2: " + str(ttest_ind(col_1_csv2, col_2_csv2)))
