import numpy as np

temperaturen = [12, 15, 14, 10, 9, 13, 11]

# Umwandlung der Liste in ein NumPy-Array
temperaturen_array = np.array(temperaturen)

# Berechnung 
durchschnitt = np.mean(temperaturen_array)
maximalwert = np.max(temperaturen_array)
minimalwert = np.min(temperaturen_array)

print("Durchschnitt:", durchschnitt)
print("Maximalwert:", maximalwert)
print("Minimalwert:", minimalwert)



print("Temperaturen als NumPy-Array:", temperaturen_array)
print("Typ:", type(temperaturen_array))

import pandas as pd

# Beispieldaten für zwei Spalten: Name und Alter
TempDaten = {
    "Tag": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
    "Temperatur": [12, 15, 14, 10, 9, 13, 11]
}

# Erstellen des DataFrames aus dem Dictionary
df = pd.DataFrame(TempDaten)

print(df)

import matplotlib.pyplot as plt

# Erstellen des Liniendiagramms
plt.plot(df.Tag, df.Temperatur, marker='o', linestyle='-', color='blue')

# Beschriftungen
plt.xlabel("Wochentage")
plt.ylabel("Temperatur (°C)")
plt.title("Temperaturen der Woche")

# Diagramm anzeigen
plt.show()