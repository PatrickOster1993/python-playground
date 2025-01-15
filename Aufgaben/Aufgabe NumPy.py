# Du bist ein Wetterforscher und möchtest die Temperaturen einer Woche analysieren. Schreibe ein Python-Skript, das die folgenden Aufgaben erfüllt:


# ## Aufgabenstellung


# ### 1. NumPy:

# - Erstelle ein NumPy-Array mit den Temperaturen (in °C) der Woche: `[12, 15, 14, 10, 9, 13, 11]`.

# - Berechne:

# - die durchschnittliche Temperatur,

# - die maximale Temperatur,

# - die minimale Temperatur.

import numpy as np

import numpy as np

# NumPy-Array mit den Temperaturen der Woche
temperaturen = np.array([12, 15, 14, 10, 9, 13, 11])

# Durchschnittliche Temperatur
durchschnitt = np.mean(temperaturen)
print(f"Durchschnittliche Temperatur: {durchschnitt:.2f}°C")

# Maximale Temperatur
max_temp = np.max(temperaturen)
print(f"Maximale Temperatur: {max_temp}°C")

# Minimale Temperatur
min_temp = np.min(temperaturen)
print(f"Minimale Temperatur: {min_temp}°C")
