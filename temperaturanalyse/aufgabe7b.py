import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import openmeteo_requests
import requests_cache
from retry_requests import retry
import datetime

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Make sure all required weather variables are listed here
url = "https://archive-api.open-meteo.com/v1/archive"
start_date = datetime.date.today() - datetime.timedelta(days=70)
end_date = datetime.date.today()

params = {
    "latitude": 51.7667,
    "longitude": 7.95,
    "start_date": start_date,
    "end_date": end_date,
    "hourly": "temperature_2m",
    "temporal_resolution": "hourly_6"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )
}

hourly_data["temperature_2m"] = hourly_temperature_2m

# Create a DataFrame from the data
hourly_dataframe = pd.DataFrame(data=hourly_data)

# Konvertiere die 'date' Spalte zu einem DatetimeIndex
hourly_dataframe["date"] = pd.to_datetime(hourly_dataframe["date"], utc=True)

# Extrahiere nur die Zeilen, die 12 Uhr an jedem Tag repräsentieren
temperatures_12pm_per_weekday = hourly_dataframe[hourly_dataframe["date"].dt.hour == 12]

# Füge die Wochentage hinzu
temperatures_12pm_per_weekday["weekday"] = temperatures_12pm_per_weekday["date"].dt.day_name()

# Definiere die Reihenfolge der Wochentage, beginnend mit Montag
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Füge die benutzerdefinierte Reihenfolge als Kategorie hinzu
temperatures_12pm_per_weekday['weekday'] = pd.Categorical(temperatures_12pm_per_weekday['weekday'], categories=weekday_order, ordered=True)

# Berechnen von Mittelwert, Maximalwert und Minimalwert
temperature_data_mean = temperatures_12pm_per_weekday.groupby("weekday")["temperature_2m"].mean()
temperature_data_max = temperatures_12pm_per_weekday.groupby("weekday")["temperature_2m"].max()
temperature_data_min = temperatures_12pm_per_weekday.groupby("weekday")["temperature_2m"].min()

# # Werte der aktuellen Woche
# today = datetime.date.today().weekday()
# today_weekday = weekday_order[today]
# temperatures_12pm_per_weekday

# current_week = {
#     "Monday": ,
#     "Tuesday": 18,
#     "Wednesday": 19,
#     "Thursday": 20,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 23
# }

# Erstellen des Tkinter-Fensters
root = tk.Tk()
root.title("Temperature Chart")

# Erstellen des Plots
fig, ax = plt.subplots(figsize=(10, 6))

# Linien für den Mittelwert
ax.plot(temperature_data_mean.index, temperature_data_mean.values, marker='o', label="Average Temperature", color='royalblue', linewidth=2)

# Scatter-Plots für Max und Min Temperaturen
ax.scatter(temperature_data_max.index, temperature_data_max.values, color='darkred', label="Max Temperature", marker='^', s=100)
ax.scatter(temperature_data_min.index, temperature_data_min.values, color='forestgreen', label="Min Temperature", marker='v', s=100)

# Achsenbezeichnungen und Titel
ax.set_xlabel("Weekdays", fontsize=12, fontweight='bold', color='black')
ax.set_ylabel("Temperature (°C)", fontsize=12, fontweight='bold', color='black')
ax.set_title("Temperatures of the Week", fontsize=14, fontweight='bold', color='black')

# Gitterlinien hinzufügen
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Achsenlimits für bessere Visualisierung
ax.set_ylim([0, 20])

# Legende
ax.legend(loc='upper right')

# Verbesserte Darstellung
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
