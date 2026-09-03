from numpy.ma.extras import average
import pandas as pd
from entsoe import EntsoePandasClient
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time

#global variables
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

load_data = pd.read_csv("elk320/elk330/ovingar/power-system-data/load/forbruk_2025.csv",sep=",",header=0,names=["datetime", "Actual Load"],parse_dates=["datetime"])

load_data["datetime"] = pd.to_datetime(load_data["datetime"], utc=True)

#Samler lastdata etter månad, og reikner ut snittlast
avg_load = load_data.groupby(load_data["datetime"].dt.month)["Actual Load"].mean().round(2)


#Skriv til fil
pd.DataFrame(avg_load.values, index=months, columns=["Gjennomsnittlig last (MW)"]).to_csv("elk320/elk330/ovingar/power-system-data/results/manedlig_last_2025.csv")

#Plotter resultatet
fig, ax = plt.subplots()
ax.plot(months, avg_load.values)
ax.set_xlabel("Månad")
ax.set_ylabel("Gjennomsnittlig last (MW)")
plt.show()

#save plot to file
fig.savefig("elk320/elk330/ovingar/power-system-data/results/manedlig_last_2025.png")
