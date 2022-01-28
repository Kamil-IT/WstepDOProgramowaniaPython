import matplotlib.pyplot as plt
import pytz
from matplotlib import pyplot

from main import get_data


df = get_data()

for i in range(df["UNIXTS"].shape[0]):
    df["UNIXTS"][i] = df["UNIXTS"][i].strftime('%H')

print(df.groupby(["UNIXTS"], as_index=False).size())

pyplot.bar([i for i in range(24)], [i[1] for i in df.groupby(["UNIXTS"], as_index=False).size().values.tolist()])
plt.show()