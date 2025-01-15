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
