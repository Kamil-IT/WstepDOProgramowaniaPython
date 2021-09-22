import multiprocessing
import random
import time

import requests


class Petitioner:
    def __init__(self, case):
        self.case = case


def go_to_window(petitioner):
    post = requests.post("http://127.0.0.1:5000/petitioner/add/" + str(petitioner.case))
    if str(post.status_code) == str(404):
        queue_not_match.put(petitioner)


def add_petitioner_to_queue():
    time_start = time.time()
    while not queue.empty():
        if queue_not_match.empty():
            petitioner = queue.get()
        else:
            petitioner = queue_not_match.get()
        go_to_window(petitioner)
        print("Queue size: " + str(queue.qsize()))
    time_end = time.time()
    print(time_end - time_start)


def is_any_window_busy():
    response = requests.get("http://127.0.0.1:5000/window/busy")
    if response.status_code == 404:
        return True
    return False


def remove_petitioner_from_window():
    while is_any_window_busy() or not queue.empty():
        requests.post("http://127.0.0.1:5000/window/" + str(random.randint(1, 3)))


def create_and_start_queue():
    add_to_queue = multiprocessing.Process(target=add_petitioner_to_queue,
                                           name="add_to_window")
    remove_from_queue = multiprocessing.Process(target=remove_petitioner_from_window,
                                                name="remove_from_window")
    add_to_queue.start()
    remove_from_queue.start()


if __name__ == '__main__':
    case_1 = 1  # A, B, C
    case_2 = 2  # C, D

    queue = multiprocessing.Queue(maxsize=800)
    queue_not_match = multiprocessing.Queue()

    for i in range(800):
        try:
            queue.put(Petitioner(random.randint(1, 2)))
        except Exception:
            print("Queue is full you can come back later")

    create_and_start_queue()
