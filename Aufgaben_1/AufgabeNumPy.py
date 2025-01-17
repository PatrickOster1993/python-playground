# NumPy:

#    Erstelle ein NumPy-Array mit den Temperaturen (in °C) der Woche: 
#    [12, 15, 14, 10, 9, 13, 11].
#    Berechne:
#    die durchschnittliche Temperatur,
#    die maximale Temperatur,
#    die minimale Temperatur.
#https://numpy.org/doc/stable/

import numpy as np

array = np.array ([12, 15, 14, 10, 9, 13, 11])

print ("Die niedrigste Temperatur beträgt : ",array.min(), "°C" )

print ("Die maximale temperatur beträgt : ",array.max(), "°C" )

print ("Die Durschnittliche temperatur beträgt : ",array.mean(), "°C" )