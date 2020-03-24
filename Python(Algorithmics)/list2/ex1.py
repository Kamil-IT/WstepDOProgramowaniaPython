import time
import random
from timeit import default_timer as timer

def bubble_sort(array):
    for passum in range(len(array) - 1, 0, -1):
        for i in range(passum):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp


def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def select_sort(array):
    for i in range(len(array)):
        min_id = i
        for j in range(i + 1, len(array)):
            if array[min_id] > array[j]:
                min_id = j
        array[i], array[min_id] = array[min_id], array[i]


def sorting_time_bubble(array):
    times = []
    for i in range(10):
        array_to_sort = array.copy()
        time_start = timer()
        bubble_sort(array_to_sort)
        time_end = timer()
        times.append(time_end - time_start)
    return max(times), sum(times) / float(len(times))


def sorting_time_insert(array):
    times = []
    for i in range(10):
        array_to_sort = array.copy()
        time_start = timer()
        insert_sort(array_to_sort)
        time_end = timer()
        times.append(time_end - time_start)
    return max(times), sum(times) / float(len(times))


def sorting_time_select(array):
    times = []
    for i in range(10):
        array_to_sort = array.copy()
        time_start = timer()
        select_sort(array_to_sort)
        time_end = timer()
        times.append(time_end - time_start)
    return max(times), sum(times) / float(len(times))


def sorting_time_all(array_size):
    array = random.sample(range(1, 1000), array_size)
    bubble_max, bubble_avg = sorting_time_bubble(array)
    insert_max, insert_avg = sorting_time_insert(array)
    select_max, select_avg = sorting_time_select(array)
    return_string = 'bubble max = ' + str(bubble_max) + ' avg= ' + str(bubble_avg) + '\n'
    return_string += 'insert max = ' + str(insert_max) + ' avg= ' + str(insert_avg) + '\n'
    return_string += 'select max = ' + str(select_max) + ' avg= ' + str(select_avg) + '\n'
    return return_string


# ex1
print(sorting_time_all(10))