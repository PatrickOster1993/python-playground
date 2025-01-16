import numpy as np
import matplotlib.pyplot as plt

# Temperaturdaten der letzten 10 Wochen (Mo-So)
temperaturen = np.array([
    [12, 15, 14, 10, 9, 13, 11],
    [11, 14, 13, 10, 8, 12, 10],
    [13, 16, 15, 11, 10, 14, 12],
    [12, 14, 15, 9, 7, 13, 11],
    [10, 13, 12, 8, 6, 11, 9],
    [11, 15, 14, 10, 11, 12, 10],
    [13, 16, 15, 11, 9, 14, 12],
    [12, 14, 13, 10, 7, 13, 11],
    [10, 13, 12, 8, 6, 11, 9],
    [11, 15, 14, 10, 8, 12, 10]
])

# Wochentage
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

# Erstelle eine Liste aller Tage in den 10 Wochen
alle_tage = [f"Woche {woche+1} - {tag}" for woche in range(10) for tag in wochentage]

# Entpacke die Temperaturwerte zu einer einzigen flachen Liste
alle_temperaturen = temperaturen.flatten()

# Berechne die Durchschnittstemperatur über alle Tage hinweg (nicht nur pro Wochentag)
durchschnitt_temperaturen = np.mean(alle_temperaturen)

# Höchst- und Tiefststand der Temperaturen über alle Tage
hoechststand = np.max(alle_temperaturen)
tiefstand = np.min(alle_temperaturen)

# Plotten aller Tage
plt.figure(figsize=(14, 8))
plt.plot(alle_tage, alle_temperaturen, marker='x', label='Temperaturen', color='blue', markersize=5)

# Durchschnittstemperatur als horizontale Linie
plt.axhline(durchschnitt_temperaturen, linestyle='--', linewidth=1, label=f'Durchschnitt: {durchschnitt_temperaturen:.2f}°C', alpha=0.6)

# Höchst- und Tiefststand markieren
plt.axhline(hoechststand, color='red', linestyle='--', label=f'Höchststand: {hoechststand}°C', linewidth=1.5)
plt.axhline(tiefstand, color='green', linestyle='--', label=f'Tiefstand: {tiefstand}°C', linewidth=1.5)

# Diagrammanpassungen
plt.title("Temperaturen der letzten 10 Wochen (Tage einzeln)", fontsize=16)
plt.xlabel("Tage", fontsize=12)
plt.ylabel("Temperatur (°C)", fontsize=12)
plt.xticks(ticks=range(0, len(alle_tage), 7), labels=alle_tage[::7], rotation=45, fontsize=10)  # Zeige nur jede 7. Beschriftung für bessere Lesbarkeit
plt.yticks(fontsize=10)
plt.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=10, loc='upper right')
plt.tight_layout()

# Diagramm anzeigen
plt.show()
