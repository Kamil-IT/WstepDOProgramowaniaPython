import multiprocessing
from collections import deque
import random


class Petitioner:
    def __init__(self, case):
        self.case = case


class Window:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.petitioner = None


def go_to_window(petitioner):
    for window in windows:
        if (window.petitioner is None) and (petitioner.case in window.type):
            window.petitioner = petitioner
    queue.put(petitioner)


def remove_from_window(petitioner):
    for window in windows:
        if window.petitioner == petitioner:
            window.petitioner = None


case_1 = 1  # A, B, C
case_2 = 2  # C, D
windows = [Window('A', [1]), Window('B', [1]), Window('C', [1, 2]), Window('D', [2])]

queue = multiprocessing.Queue(maxsize=800)

for i in range(random.randint(100, 900)):
    try:
        queue.put(Petitioner(random.randint(1, 2)))
    except Exception:
        print("Queue is full you can come back later")


def add_petitioner_to_queue():
    while not queue.empty():
        # TODO: add que to list
        petitioner = queue.get()
        go_to_window(petitioner)
        print("Queue size: " + str(queue.qsize()))


def remove_petitioner_from_window():
    is_window_working = True
    while not queue.empty() or is_window_working:
        windows[random.randint(0, 3)].petitioner = None
        for i in range(len(windows)):
            if windows[i].petitioner is not None:
                is_window_working = True
                break
            elif i == len(windows) - 1:
                is_window_working = False
        message = ""
        for window in windows:
            message += f'Window type:{window.type} petitioner:{window.petitioner} '
        print(f'Queue size {queue.qsize()} ' + message)


add_to_queue = multiprocessing.Process(target=add_petitioner_to_queue,
                                       name="add_to_window")

remove_from_queue = multiprocessing.Process(target=remove_petitioner_from_window,
                                            name="remove_from_window")
add_to_queue.start()
remove_from_queue.start()
