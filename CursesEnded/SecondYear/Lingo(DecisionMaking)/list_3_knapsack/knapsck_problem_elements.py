import itertools
import numpy as np


def is_out_of_possible_val(item_backpack, Quantity_el):
    for i in range(len(Quantity_el)):
        if item_backpack[i] > Quantity_el[i]:
            return True
    return False


def knap_sack(V, Quantity_el, val):

    max_value_backpack = 0
    l = [i + 1 for i in range(max(Quantity_el))]
    for item_backpack in list(itertools.product(l, repeat=len(val))):
        if is_out_of_possible_val(item_backpack, Quantity_el):
            continue
        if sum(item_backpack) <= V:
            if max_value_backpack < sum(np.array(item_backpack) * val):
                max_value_backpack = sum(np.array(item_backpack) * val)
    return max_value_backpack


def knap_sack_elements_in_r(V, Quantity_el, val):

    max_value_backpack = 0
    l = np.linspace(0, max(Quantity_el), 100)
    for item_backpack in list(itertools.product(l, repeat=len(val))):
        if is_out_of_possible_val(item_backpack, Quantity_el):
            continue
        if sum(item_backpack) <= V:
            if max_value_backpack < sum(np.array(item_backpack) * val):
                max_value_backpack = sum(np.array(item_backpack) * val)
    return max_value_backpack


# Value of item
val = [60, 100, 120]
# Size of item
Quantity_el = [2, 4, 11]
# Backpack size
V = 10

print(knap_sack(V, Quantity_el, val))
print(knap_sack_elements_in_r(V, Quantity_el, val))
