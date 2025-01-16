# ### 3. Matplotlib:

# - Erstelle ein einfaches Liniendiagramm, das die Temperatur über die Tage darstellt.

# - Beschrifte die Achsen:

# -  **x-Achse**: Wochentage.

# -  **y-Achse**: Temperatur (°C).

# - Gib dem Diagramm einen Titel, z. B. "Temperaturen der Woche".

# - Füge eine horizontale Linie in das Diagramm ein, die den Durchschnitt der Temperaturen darstellt.

  

# ## Erwartetes Ergebnis

# -  **Konsolenausgabe:** Durchschnitt, maximale und minimale Temperatur sowie die Tabelle.

# -  **Diagramm:** Eine anschauliche Visualisierung der Temperaturen über die Woche.

print("Aufgabe 3")

import matplotlib.pyplot as plt  # Importieren der Matplotlib-Bibliothek
import numpy as np  # Importieren der NumPy-Bibliothek
import pandas as pd  # Importieren der Pandas-Bibliothek

# Erstellen eines NumPy-Arrays mit den Temperaturen der Woche
temperatures = np.array([12, 15, 14, 10, 9, 13, 11])

# Berechnen der durchschnittlichen Temperatur
average_temperature = np.mean(temperatures)

# Berechnen der maximale Temperatur
max_temperature = np.max(temperatures)

# Berechnen der minimale Temperatur
min_temperature = np.min(temperatures)

# Erstellen eines Pandas-DataFrames mit zwei Spalten
data = {
    "Tag": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
    "Temperatur": [12, 15, 14, 10, 9, 13, 11]
}
df = pd.DataFrame(data)

# Erstellen eines Matplotlib-Diagramms
fig, ax = plt.subplots()
ax.plot(df["Tag"], df["Temperatur"], marker='o')

# Beschriften der Achsen
ax.set_xlabel("Tag")
ax.set_ylabel("Temperatur (°C)")

# Beschriften des Diagramms
ax.set_title("Temperaturen der Woche")

# Füge eine horizontale Linie in das Diagramm ein
ax.axhline(y=average_temperature, color='r', linestyle='--')

# Zeichnen des Diagramms
plt.show()