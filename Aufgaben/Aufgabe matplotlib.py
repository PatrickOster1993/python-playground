import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Daten für die Wochentage und Temperaturen
tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
temperaturen = [12, 15, 14, 10, 9, 13, 11]

# Durchschnittstemperatur berechnen
durchschnitt = np.mean(temperaturen)

# Erstellen des Liniendiagramms
plt.plot(tage, temperaturen, marker='o', label='Temperatur')

# Hinzufügen einer horizontalen Linie für den Durchschnitt
plt.axhline(y=durchschnitt, color='red', linestyle='--', label=f'Durchschnitt: {durchschnitt:.2f}°C')

# Beschriftung der Achsen
plt.xlabel("Wochentage")
plt.ylabel("Temperatur (°C)")

# Titel des Diagramms
plt.title("Temperaturen der Woche")

# Legende hinzufügen
plt.legend()

# Diagramm anzeigen
plt.show()
