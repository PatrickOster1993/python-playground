#Temperaturanalyse

#1. NumPy:
#Erstelle ein NumPy-Array mit den Temperaturen (in °C) der Woche: [12, 15, 14, 10, 9, 13, 11].
#Berechne: die durchschnittliche Temperatur, die maximale Temperatur, die minimale Temperatur.

import numpy as np

Temp = [12, 15, 14, 10, 9, 13, 11]
array = np.array(Temp)

Durchschnitt = np.mean(Temp)
max_Temp = np.max(Temp)
min_Temp = np.min(Temp)

print(f"Die Durchschittstemperatur beträgt {Durchschnitt} Grad.")
print(f"Die maximale Temperatur beträgt {max_Temp} Grad.")
print(f"Die mainimale Temperatur beträgt {min_Temp} Grad.")

