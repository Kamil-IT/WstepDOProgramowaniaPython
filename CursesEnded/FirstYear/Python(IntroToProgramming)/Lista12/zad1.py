import matplotlib.pyplot as plt
import numpy as np
import pandas
from matplotlib import gridspec
import matplotlib as mpl



file_price_water = pandas.read_csv('ceny_wody_zimnej_za_1m.csv')
data_price_water = file_price_water[['Kod', 'Nazwa', 'ZimnaWoda']]

file_work_places = pandas.read_csv('liczba_miejsc_pracy.csv')
data_work_places = file_work_places[['Kod', 'Nazwa', 'NoweMiejscaPracy', 'ZlikwidowaneMiejscaPracy']]

voivodeship_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
# Voivodeship - wojewodztwo

new_work_places = 0.0
for place in data_work_places.NoweMiejscaPracy:
    new_work_places += place

lost_work_places = 0.0
for place in data_work_places.ZlikwidowaneMiejscaPracy:
    lost_work_places += place

# Set style
mpl.style.use('seaborn')

# Init figure and space for plots
fig = plt.figure(constrained_layout=False, figsize=(15, 10))
spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)

# Init charts
ax1 = fig.add_subplot(spec2[0, 0])
ax1.plot(data_price_water.ZimnaWoda, data_price_water.Nazwa, 'g', label='Price')
ax1.grid(True)
ax1.set_xlabel('Price')
ax1.set_title('Price for 1m3 cold water in voivodeship')
ax1.legend()

ax2 = fig.add_subplot(spec2[0, 1])
ax2.bar(voivodeship_numbers, data_price_water.ZimnaWoda,  label='Price')
ax2.set_xlabel('Number of voivodeship')
ax2.set_title('Price for 1m3 cold water in voivodeship')
ax2.legend()


ax3 = fig.add_subplot(spec2[1, 0])
ax3.pie([new_work_places, lost_work_places],
        explode=(0.1, 0),
        labels=['New work places', 'Lost work places'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['orange', 'cyan'])
ax3.set_title("Work places")
ax3.legend()


ax4 = fig.add_subplot(spec2[1, 1])
ax4.scatter(file_work_places.ZlikwidowaneMiejscaPracy,
            file_work_places.NoweMiejscaPracy,
            label='value y= new, value x= lost')
ax4.set_title("List of work places")
ax4.set_xlabel("Lost work places[k]")
ax4.set_ylabel("New wok places[k]")
ax4.legend()

plt.show()