# Types in python

integer_ = 10
bool_ = True
float_ = 1.0
bytes_ = b"Hello"
complex_ = 1j

string_ = "asdasd"

list_str = ["one", "two", "three"]
set_str = {"one", "two", "three"}
tuple_str = ("one", "two", "three")
dictionary_ = {"name": "John", "age": 36}

range_ = range(6)

# If for while
i = 1
if i == 1:
    print(i)

for e in range(5):
    print(e)

f = 1
while f < 6:
    f += 1

# Libraries
import numpy as np
import matplotlib.pyplot as plt

np.random.randint(1, 5)

x = np.array([10, 20, 30, 40, 50])
y = np.array([30, 45, 20, 60, 24])
plt.plot(x, y, marker="o")
# plt.show()

linspace_x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
plt.plot(linspace_x, np.sin(linspace_x))
plt.show()
