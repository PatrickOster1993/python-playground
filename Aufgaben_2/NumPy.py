"""
### 1. NumPy: https://numpy.org/doc/2.2/user/quickstart.html

- Erstelle ein NumPy-Array mit den Temperaturen (in °C) der Woche: `[12, 15, 14, 10, 9, 13, 11]`.

- Berechne:

- die durchschnittliche Temperatur,

- die maximale Temperatur,

- die minimale Temperatur.
"""

#libary import
import numpy as np

# Temperaturdaten
temperaturen = np.array([12, 15, 14, 10, 9, 13, 11])

# Berechnungen der Temperatur
durchschnitt = np.mean(temperaturen)
max_temp = np.max(temperaturen)
min_temp = np.min(temperaturen)

# Ausgabe
print(f"Durchschnittstemperatur: {durchschnitt:.2f}°C")
print(f"Maximaltemperatur: {max_temp}°C")
print(f"Minimaltemperatur: {min_temp}°C")

# Output Ergebnisse sollen so aussehn
# Durchschnittstemperatur: 12.00°C
# Maximaltemperatur: 15°C
# Minimaltemperatur: 9°C
