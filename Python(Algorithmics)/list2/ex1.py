import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt


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


def sorting_time_all_10_1000_draw_plot():
    # init array
    arrays = [random.sample(range(1, 1000), 10),
              random.sample(range(1, 1000), 20),
              random.sample(range(1, 1000), 50),
              random.sample(range(1, 1000), 100),
              random.sample(range(1, 1000), 200),
              random.sample(range(1, 1000), 500),
              [random.randint(1, 1000) for i in range(1000)]]
    # init arrays to save scores
    bubble_avg, insert_avg, select_avg = [], [], []
    bubble_max, insert_max, select_max = [], [], []

    for array in arrays:
        max_time, avg_time = sorting_time_bubble(array)
        bubble_max.append(max_time)
        bubble_avg.append(avg_time)

        max_time, avg_time = sorting_time_insert(array)
        insert_max.append(max_time)
        insert_avg.append(avg_time)

        max_time, avg_time = sorting_time_select(array)
        select_max.append(max_time)
        select_avg.append(avg_time)

    array_size_x = [10, 20, 50, 100, 200, 500, 1000]

    fig, ax = plt.subplots()
    ax.plot(bubble_avg, array_size_x, 'r', label='bąbelkowy avg')
    ax.plot(insert_avg, array_size_x, 'b', label='wstawianie avg')
    ax.plot(select_avg, array_size_x, 'g', label='wybór avg')
    ax.plot(bubble_max, array_size_x, 'r*', label='bąbelkowy max')
    ax.plot(insert_max, array_size_x, 'b*', label='wstawianie max')
    ax.plot(select_max, array_size_x, 'g*', label='wybór max')
    plt.title('czas działania algorytmów')
    plt.xlabel('czas')
    plt.ylabel('długości list')
    plt.legend()
    plt.show()


def bubble_sort_changed_1(array):
    for passum in range(len(array) - 1, 0, -1):
        old_array = array.copy()
        for i in range(passum):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        if old_array == array:
            break


def bubble_sort_from_link(array):
    for i in range(len(array)):
        for j in range(0, (len(array) - 1) - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def bubble_sort_change_1(array):
    for i in range(len(array)):
        old_arr = array.copy()
        for j in range(0, (len(array) - 1) - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
        if old_arr == array:
            break


def bubble_sort_change_2(array):
    for i in range(len(array)):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def time_sorting_3_bubble_sort(array_size):
    array = random.sample(range(1, 1000), array_size)

    time_start = timer()
    bubble_sort_from_link(array)
    time_end = timer()
    bubble_time = time_end - time_start

    time_start = timer()
    bubble_sort_change_1(array)
    time_end = timer()
    bubble1_time = time_end - time_start

    time_start = timer()
    bubble_sort_change_2(array)
    time_end = timer()
    bubble2_time = time_end - time_start

    return_string = 'bubble time = ' + str(bubble_time) + '\n'
    return_string += 'bubble changed 1 time = ' + str(bubble1_time) + '\n'
    return_string += 'bubble changed 2 time = ' + str(bubble2_time) + '\n'
    return return_string


# ex1
print(sorting_time_all(10))

# ex2
sorting_time_all_10_1000_draw_plot()

# ex3
print(time_sorting_3_bubble_sort(10))
