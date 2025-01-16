import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tempdata = [
    {
        "Kalenderweek": 1,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [11, 9, 12, 10, 13, 10, 12],
        "Max": [14, 12, 15, 13, 16, 14, 15],
        "Min": [6, 5, 7, 6, 8, 6, 7]
    },
    {
        "Kalenderweek": 2,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [12, 14, 13, 11, 10, 12, 14],
        "Max": [15, 17, 16, 14, 13, 15, 17],
        "Min": [7, 8, 9, 8, 6, 7, 8]
    },
    {
        "Kalenderweek": 3,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [14, 15, 13, 12, 14, 15, 16],
        "Max": [17, 18, 16, 15, 17, 18, 19],
        "Min": [9, 10, 8, 9, 10, 11, 12]
    },
    {
        "Kalenderweek": 4,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [15, 14, 16, 15, 17, 16, 15],
        "Max": [18, 17, 19, 18, 20, 19, 18],
        "Min": [10, 9, 11, 10, 12, 11, 10]
    },
    {
        "Kalenderweek": 5,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [17, 18, 17, 16, 19, 18, 17],
        "Max": [20, 21, 20, 19, 22, 21, 20],
        "Min": [12, 13, 12, 11, 14, 13, 12]
    },
    {
        "Kalenderweek": 6,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [18, 19, 18, 17, 20, 19, 18],
        "Max": [21, 22, 21, 20, 23, 22, 21],
        "Min": [13, 14, 13, 12, 15, 14, 13]
    },
    {
        "Kalenderweek": 7,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [19, 18, 20, 19, 21, 20, 19],
        "Max": [22, 21, 23, 22, 24, 23, 22],
        "Min": [14, 13, 15, 14, 16, 15, 14]
    },
    {
        "Kalenderweek": 8,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [20, 21, 19, 18, 22, 21, 20],
        "Max": [23, 24, 22, 21, 25, 24, 23],
        "Min": [15, 16, 14, 13, 17, 16, 15]
    },
    {
        "Kalenderweek": 9,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [22, 23, 21, 20, 24, 23, 22],
        "Max": [25, 26, 24, 23, 27, 26, 25],
        "Min": [17, 18, 16, 15, 19, 18, 17]
    },
    {
        "Kalenderweek": 10,
        "Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Temp": [24, 25, 23, 22, 26, 25, 24],
        "Max": [27, 28, 26, 25, 29, 28, 27],
        "Min": [19, 20, 18, 17, 21, 20, 19]
    }
]
def calculate_average_temps(tempdata):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_totals = {day: {"Temp": 0, "Max": 0, "Min": 0} for day in days}
    day_counts = {day: 0 for day in days}

    for week in tempdata:
        for day, temp, max_temp, min_temp in zip(week["Tage"], week["Temp"], week["Max"], week["Min"]):
            day_totals[day]["Temp"] += temp
            day_totals[day]["Max"] += max_temp
            day_totals[day]["Min"] += min_temp
            day_counts[day] += 1

    avg_temps = {day: {
        "Temp": day_totals[day]["Temp"] / day_counts[day],
        "Max": day_totals[day]["Max"] / day_counts[day],
        "Min": day_totals[day]["Min"] / day_counts[day]
    } for day in days}

    return avg_temps

# Gebruik de functie
average_temps = calculate_average_temps(tempdata)

# Print de resultaten
for day, temps in average_temps.items():
    print(f"{day}:")
    print(f"  Gemiddelde temp: {temps['Temp']:.2f}")
    print(f"  Gemiddelde max: {temps['Max']:.2f}")
    print(f"  Gemiddelde min: {temps['Min']:.2f}")

# Voor het plotten (met matplotlib bijvoorbeeld):
plt.figure(figsize=(12, 6))
plt.style.use('dark_background')

x = list(average_temps.keys())
y_temp = [temps['Temp'] for temps in average_temps.values()]
y_max = [temps['Max'] for temps in average_temps.values()]
y_min = [temps['Min'] for temps in average_temps.values()]

plt.plot(x, y_temp, marker='o', label='Average Temp')
plt.plot(x, y_max, marker='s', label='Average Max')
plt.plot(x, y_min, marker='^', label='Average Min')

plt.title("Average temperatures per weekday van de week")
plt.xlabel("Day of week")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()