import numpy as np
from scipy import signal
import pandas as pd


N = 1000
t = np.sort(np.random.uniform(0, 10, N))
sin = pd.Series(np.sin(5 * np.pi * t))
# sawtooth = signal.sawtooth(np.pi * 5 * t)
# square = signal.square(np.pi * 5 * t)

step = 80
st = 0.25

start = 0
end = step
while True:
    window = sin[start: end]
    print(f'{start} - {end} mean {window.mean()} min {window.min()} max {window.max()} std {window.std()}')
    start = int(end - step * st)
    end = int(start + step)
    if end > N:
        break
