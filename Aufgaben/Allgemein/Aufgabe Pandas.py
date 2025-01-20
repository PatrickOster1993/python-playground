# ### 2. Pandas:

# - Erstelle ein Pandas-DataFrame mit zwei Spalten:

# -  **Tag**: Die Wochentage ("Montag", "Dienstag", "Mittwoch ...).

# -  **Temperatur**: Die oben erstellten Temperaturen.

# - Gib die Tabelle in der Konsole aus.


import pandas as pd

tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
temperaturen = [12, 15, 14, 10, 9, 13, 11]

data = {
    "Tag": tage,
    "Temperatur (°C)": temperaturen
}
df = pd.DataFrame(data)

print(df)


# Liste der Wochentage und Temperaturen:

# tage enthält die Namen der Wochentage.
# temperaturen enthält die Temperaturen der Woche.
# DataFrame erstellen:

# pd.DataFrame(data) erstellt eine Tabelle mit den beiden Spalten Tag und Temperatur (°C).
# Ausgabe des DataFrames:

# print(df) gibt die Tabelle in der Konsole aus.