import numpy as np
import matplotlib.pyplot as plt

# Beispielhafte Temperaturdaten (in °C) der letzten 10 Kalenderwochen (Mo - So)
temperaturen = np.array([
    [10, 12, 13, 15, 14, 12, 10],  # Woche 1
    [11, 13, 14, 16, 15, 13, 11],  # Woche 2
    [12, 14, 15, 17, 16, 14, 12],  # Woche 3
    [13, 15, 16, 18, 17, 15, 13],  # Woche 4
    [14, 16, 17, 19, 18, 16, 14],  # Woche 5
    [13, 15, 16, 18, 17, 15, 13],  # Woche 6
    [12, 14, 15, 17, 16, 14, 12],  # Woche 7
    [11, 13, 14, 16, 15, 13, 11],  # Woche 8
    [10, 12, 13, 15, 14, 12, 10],  # Woche 9
    [9, 11, 12, 14, 13, 11, 9],    # Woche 10
])

# Berechnung der Durchschnittstemperatur für jeden Wochentag (Mo - So)
durchschnittstemperaturen = np.mean(temperaturen, axis=0)

# Bestimmung des Höchst- und Tiefstwerts der Durchschnittstemperaturen
max_temp = np.max(durchschnittstemperaturen)
min_temp = np.min(durchschnittstemperaturen)

# Wochentage
wochentage = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']

# Erstellen des Diagramms
plt.figure(figsize=(10, 6))
plt.plot(wochentage, durchschnittstemperaturen, marker='o', color='b', label='Durchschnittstemperatur', linestyle='-', linewidth=2)

# Hinzufügen von Höchst- und Tiefstwerten als gestrichelte Linien
plt.axhline(max_temp, color='r', linestyle='--', label=f'Höchstwert: {max_temp}°C')
plt.axhline(min_temp, color='g', linestyle='--', label=f'Tiefstwert: {min_temp}°C')

# Titel und Achsenbeschriftungen
plt.title('Durchschnittstemperaturen der letzten 10 Wochen', fontsize=16)
plt.xlabel('Wochentage', fontsize=14)
plt.ylabel('Temperatur (°C)', fontsize=14)

# Legende hinzufügen
plt.legend()

# Gitter für besseres Ablesen hinzufügen
plt.grid(True, linestyle='--', alpha=0.6)

# Layout anpassen für bessere Darstellung
plt.tight_layout()

# Diagramm anzeigen
plt.show()
