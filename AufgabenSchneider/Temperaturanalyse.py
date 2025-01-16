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

#Erstelle ein Pandas-DataFrame mit zwei Spalten:
#Tag: Die Wochentage ("Montag", "Dienstag", "Mittwoch ...).
#Temperatur: Die oben erstellten Temperaturen.
#Gib die Tabelle in der Konsole aus.

import pandas as pd

tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

df = pd.DataFrame({
    "Tag": tage,
    "Temperatur": Temp
})

print(df)

# Matplotlib:
# Erstelle ein einfaches Liniendiagramm, das die Temperatur über die Tage darstellt.
# Beschrifte die Achsen:
# x-Achse: Wochentage.
# y-Achse: Temperatur (°C).
# Gib dem Diagramm einen Titel, z. B. "Temperaturen der Woche".
# Füge eine horizontale Linie in das Diagramm ein, die den Durchschnitt der Temperaturen darstellt.

import matplotlib.pyplot as plt

#Liniendiagramm erstellen
plt.figure(figsize=(8,5)) #Größe des Diagramms
plt.plot(tage, Temp, marker ='o', label='Temperatur', color='blue')

# Horizontale Linie für den Durchschnitt
plt.axhline(y=Durchschnitt, color='red', linestyle='--', label=f'Durchschnitt: {Durchschnitt:.1f}°C')

# Diagramm beschriften
plt.title("Temperaturen der Woche")
plt.xlabel("Wochentage")
plt.ylabel("Temperatur (°C)")
plt.legend()  # Legende anzeigen
plt.grid(True, linestyle='--', alpha=0.5)  # Rasterlinien hinzufügen

Diagramm anzeigen
plt.tight_layout()  # Layout anpassen
plt.show()