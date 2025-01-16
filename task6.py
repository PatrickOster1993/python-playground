# # Übungsaufgabe: Temperaturanalyse

# Du bist ein Wetterforscher und möchtest die Temperaturen einer Woche analysieren. Schreibe ein Python-Skript, das die folgenden Aufgaben erfüllt:


# ## Aufgabenstellung

# ### 1. NumPy:

# - Erstelle ein NumPy-Array mit den Temperaturen (in °C) der Woche: `[12, 15, 14, 10, 9, 13, 11]`.

# - Berechne:

# - die durchschnittliche Temperatur,

# - die maximale Temperatur,

# - die minimale Temperatur.

print("Aufgabe 1")

import numpy as np  # Importieren der NumPy-Bibliothek

# Erstellen eines NumPy-Arrays mit den Temperaturen der Woche
temperatures = np.array([12, 15, 14, 10, 9, 13, 11])

# Berechnen der durchschnittlichen Temperatur
average_temperature = np.mean(temperatures)

# Berechnen der maximale Temperatur
max_temperature = np.max(temperatures)

# Berechnen der minimale Temperatur
min_temperature = np.min(temperatures)

print(f"Durchschnittliche Temperatur: {average_temperature:.2f}°C")
print(f"Maximale Temperatur: {max_temperature}°C")
print(f"Minimale Temperatur: {min_temperature}°C")