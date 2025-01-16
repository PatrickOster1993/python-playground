# ### 2. Pandas:

# - Erstelle ein Pandas-DataFrame mit zwei Spalten:

# -  **Tag**: Die Wochentage ("Montag", "Dienstag", "Mittwoch ...).

# -  **Temperatur**: Die oben erstellten Temperaturen.

# - Gib die Tabelle in der Konsole aus.

print("Aufgabe 2")

import pandas as pd  # Importieren der Pandas-Bibliothek

# Erstellen eines Pandas-DataFrames mit zwei Spalten
data = {
    "Tag": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
    "Temperatur": [12, 15, 14, 10, 9, 13, 11],
    "Jahrezeit": ["Fruehjahr", "Karneval", "Ostern", "Sommer", "Herbst", "Winter", "Weihnachten"]
}
df = pd.DataFrame(data)

# Ausgabe des DataFrames
print(df)
