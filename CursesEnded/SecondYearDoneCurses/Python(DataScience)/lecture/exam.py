def is_elent_same(list1, list2):
    for el in list1:
        for el2 in list2:
            if el == el2:
                return True

    return False


list1 = [1, 2, 3]

list2 = [5, 6, 7, 4, 8]

print(is_elent_same(list1, list2))
