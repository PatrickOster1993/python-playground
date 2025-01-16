import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NumPy
temperaturen = np.array([12, 15, 14, 10, 9, 13, 11])

# Berechnungen der Temperaturwerte
durchschnitt = np.mean(temperaturen)
max_temp = np.max(temperaturen)
min_temp = np.min(temperaturen)

print(f"Durchschnittliche Temperatur: {durchschnitt:.2f} °C")
print(f"Maximale Temperatur: {max_temp} °C")
print(f"Minimale Temperatur: {min_temp} °C")

# 2. Pandas
# Erstelle einen Pandas DataFrame mit den Wochentagen und den Temperaturen
tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
df = pd.DataFrame({
    'Tag': tage,
    'Temperatur': temperaturen
})

# Gib die Tabelle aus
print("\nTemperatur-Tabelle der Woche:")
print(df)

# 3. Matplotlib
# Erstelle das Liniendiagramm
plt.plot(tage, temperaturen, marker='o', color='b', label='Temperatur')

# Horizontale Linie für den Durchschnitt
plt.axhline(y=durchschnitt, color='r', linestyle='--', label=f'Durchschnitt ({durchschnitt:.2f}°C)')

# Diagramm beschriften
plt.xlabel('Wochentage')
plt.ylabel('Temperatur (°C)')
plt.title('Temperaturen der Woche')
plt.legend()

# Diagramm anzeigen
plt.grid(True)
plt.show()