def bubble_sort(unsorted_list):
    sorted_list = unsorted_list
    for iter_num in range(len(sorted_list) - 1, 0, -1):
        for idx in range(iter_num):
            if sorted_list[idx] >= sorted_list[idx + 1]:
                temp = sorted_list[idx]
                sorted_list[idx] = sorted_list[idx + 1]
                sorted_list[idx + 1] = temp
    return sorted_list


def insertion_sort(unsorted_list):
    sorted_list = unsorted_list
    for i in range(1, len(sorted_list)):
        j = i - 1
        nxt_element = sorted_list[i]
    while (sorted_list[j] > nxt_element) and (j >= 0):
        sorted_list[j + 1] = sorted_list[j]
        j = j - 1
    sorted_list[j + 1] = nxt_element
    return sorted_list


def shell_sort(unsorted_list):
    sorted_list = unsorted_list
    gap = len(sorted_list) // 2
    while gap > 0:
        for i in range(gap, len(sorted_list)):
            temp = sorted_list[i]
            j = i
        while j >= gap and sorted_list[j - gap] > temp:
            sorted_list[j] = sorted_list[j - gap]
            j = j - gap
            sorted_list[j] = temp
        gap = gap // 2
    return sorted_list


def sort(unsorted_list):
    if len(unsorted_list) < 5:
        return insertion_sort(unsorted_list)
    elif len(unsorted_list) < 20:
        return bubble_sort(unsorted_list)
    else:
        return shell_sort(unsorted_list)
