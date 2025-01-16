"""
### 3. Matplotlib: https://matplotlib.org/stable/

- Erstelle ein einfaches Liniendiagramm, das die Temperatur über die Tage darstellt.

- Beschrifte die Achsen:

-  **x-Achse**: Wochentage.

-  **y-Achse**: Temperatur (°C).

- Gib dem Diagramm einen Titel, z. B. "Temperaturen der Woche".

- Füge eine horizontale Linie in das Diagramm ein, die den Durchschnitt der Temperaturen darstellt.
"""

import matplotlib.pyplot as plt

# Beispiel-Daten
tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag","Samstag","Sonntag"]
temperaturen = [9,16,6,17,13,19,32]

# Diagramm erstellen
plt.plot(tage, temperaturen)
plt.title("Temperaturen der Woche")
plt.xlabel("Tage")
plt.ylabel("Temperatur (°C)")
plt.show()