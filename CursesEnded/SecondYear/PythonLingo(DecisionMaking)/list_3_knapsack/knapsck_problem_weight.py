import itertools
import numpy as np


def knap_sack(V, V_el, val):

    max_value_backpack = 0
    l = [False, True]
    for item_backpack in list(itertools.product(l, repeat=len(val))):
        if sum(np.array(item_backpack) * np.array(V_el)) <= V:
            if max_value_backpack < sum(np.array(item_backpack) * val):
                max_value_backpack = sum(np.array(item_backpack) * val)
    return max_value_backpack


def knap_sack_elements_in_r(V, V_el, val):

    max_value_backpack = 0
    l = np.linspace(0.0, 1.0, 100)
    for item_backpack in list(itertools.product(l, repeat=len(val))):
        if sum(np.array(item_backpack) * np.array(V_el)) <= V:
            if max_value_backpack < sum(np.array(item_backpack) * val):
                max_value_backpack = sum(np.array(item_backpack) * val)
    return max_value_backpack


# Value of item
val = [60, 100, 120]
# Size of item
V_el = [10, 20, 30]
# Backpack size
V = 50

print(knap_sack(V, V_el, val))
print(knap_sack_elements_in_r(V, V_el, val))
