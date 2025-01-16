import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Analyse der Temperaturen
temperatures = np.array([12, 15, 14, 10, 9, 13, 11])

# Statistische Berechnungen
mean = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

# Konsolenausgaben
print(f"Durchschnittliche Temperatur: {mean:}°C")
print(f"Max. Temperatur: {max_temp}°C")
print(f"Min. Temperatur: {min_temp}°C")

# DataFrame erstellen
wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
df = pd.DataFrame({"Tag": wochentage, "Temperatur (°C)": temperatures})

# DataFrame in Konsole ausgeben
print("\nDataFrame:")
print(df)

# Plotten
plt.style.use('dark_background')
plt.figure(figsize=(8, 5))
plt.plot(wochentage, temperatures, marker='o', label='Temperatur', color='#F9C0AB')

# Durchschnitt als horizontale Linie einzeichnen
plt.axhline(y=mean, color='#ABE4F9', linestyle=':', label=f'Durchschnittstemperatur')

# Achsenbeschriftung
plt.xlabel("Wochentag")
plt.ylabel("Temperatur (°C)")
plt.title("Aufgabe 7: Temperaturanalyse")
plt.legend()

# Gitternetz hinzufügen
plt.grid(axis='y', linewidth=0.5, alpha=0.25)

# Diagramm anzeigen
plt.show()

# Frage: Was müssten wir ändern, damit das Diagramm als Art "Vorhersagemodell gültig wäre? (= selbständige Aufgabe)