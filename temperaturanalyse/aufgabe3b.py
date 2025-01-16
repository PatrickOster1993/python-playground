import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

temperature_data = {
    "Montag": [8, 9, 10, 7, 6, 5, 4, 3, 5, 4],  
    "Dienstag": [9, 10, 11, 8, 7, 6, 5, 4, 6, 5],
    "Mittwoch": [10, 11, 12, 9, 8, 7, 6, 5, 7, 6],
    "Donnerstag": [11, 12, 13, 10, 9, 8, 7, 6, 8, 7],
    "Freitag": [12, 13, 14, 11, 10, 9, 8, 7, 9, 8],
    "Samstag": [13, 14, 15, 12, 11, 10, 9, 8, 10, 9],
    "Sonntag": [14, 15, 16, 13, 12, 11, 10, 9, 11, 10]
}

temperature_data_mean = {
    "Montag": np.mean(temperature_data["Montag"]),  
    "Dienstag": np.mean(temperature_data["Dienstag"]),
    "Mittwoch": np.mean(temperature_data["Mittwoch"]),
    "Donnerstag": np.mean(temperature_data["Donnerstag"]),
    "Freitag": np.mean(temperature_data["Freitag"]),
    "Samstag": np.mean(temperature_data["Samstag"]),
    "Sonntag": np.mean(temperature_data["Sonntag"])
}

temperature_data_max = {
    "Montag": np.max(temperature_data["Montag"]),
    "Dienstag": np.max(temperature_data["Dienstag"]),
    "Mittwoch": np.max(temperature_data["Mittwoch"]),
    "Donnerstag": np.max(temperature_data["Donnerstag"]),
    "Freitag": np.max(temperature_data["Freitag"]),
    "Samstag": np.max(temperature_data["Samstag"]),
    "Sonntag": np.max(temperature_data["Sonntag"])
}

temperature_data_min = {
    "Montag": np.min(temperature_data["Montag"]),
    "Dienstag": np.min(temperature_data["Dienstag"]),
    "Mittwoch": np.min(temperature_data["Mittwoch"]),
    "Donnerstag": np.min(temperature_data["Donnerstag"]),
    "Freitag": np.min(temperature_data["Freitag"]),
    "Samstag": np.min(temperature_data["Samstag"]),
    "Sonntag": np.min(temperature_data["Sonntag"])
}

root = tk.Tk()
root.title("Temperature Chart")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(list(temperature_data.keys()), list(temperature_data_mean.values()), marker='o', label="Temperature", color='blue')
ax.scatter(list(temperature_data.keys()), list(temperature_data_max.values()), color='red', label="Max Temperature", marker='^')
ax.scatter(list(temperature_data.keys()), list(temperature_data_min.values()), color='green', label="Min Temperature", marker='v')

ax.set_xlabel("Weekdays")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Temperatures of the Week")
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
