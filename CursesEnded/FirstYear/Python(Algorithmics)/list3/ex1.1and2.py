import queue
from random import randint, choice


class OfficeWindow:
    def __init__(self, window_type, time):
        self.type = window_type
        self.time = time


class Client:
    def __init__(self, case_type, complexity):
        self.type = case_type
        self.complexity = complexity


class Office:
    def __init__(self):
        self.windows = []

    def init_10_window_random_time(self):
        self.windows.append(OfficeWindow('A', randint(1, 100)))
        self.windows.append(OfficeWindow('A', randint(1, 100)))
        self.windows.append(OfficeWindow('A', randint(1, 100)))
        self.windows.append(OfficeWindow('B', randint(1, 100)))
        self.windows.append(OfficeWindow('B', randint(1, 100)))
        self.windows.append(OfficeWindow('B', randint(1, 100)))
        self.windows.append(OfficeWindow('C', randint(1, 100)))
        self.windows.append(OfficeWindow('C', randint(1, 100)))
        self.windows.append(OfficeWindow('C', randint(1, 100)))
        self.windows.append(OfficeWindow('E', randint(1, 100)))

    def print_all_windows(self):
        for window in self.windows:
            print(f'Window type:{window.type} time:{window.time}')


# ex 1.1
office = Office()
office.init_10_window_random_time()
office.print_all_windows()

# ex 1.2
que = queue.Queue()
# Create queue
for i in range(0, 30):
    que.put(
        Client(
            choice(('A', 'B', 'C')),
            randint(1, 10)))
# Show queue
for i in range(0, que.qsize()):
    client = que.get()
    print(f'Client nr{i+1}: complexity:{client.complexity} type:{client.type}')

