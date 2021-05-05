def quick_sort(array=[12, 4, 5, 6, 7, 3, 1, 15]):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)
    return quick_sort(less) + equal + quick_sort(greater)


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break
    return array