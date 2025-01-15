"""
### 2. Pandas:
- Erstelle ein Pandas-DataFrame mit zwei Spalten:
-  **Tag**: Die Wochentage ("Montag", "Dienstag", "Mittwoch ...).
-  **Temperatur**: Die oben erstellten Temperaturen.
- Gib die Tabelle in der Konsole aus.
"""

#Bibliothek imprtieren
import pandas as pd
import sys #für sys.version
print(sys.version)
print('python version', sys.version) #kleine Spielrei um zusehn welche python version aktuell vorhanden ist
print('pandas version', pd.__version__) # ebendfalls um nachzuvollziehen welche panda version vorhanden ist

print() #Leere Zeile für Übersicht

# Daten erstellen 
# !!! sind keine Arrays sondern Python-Listen erkennbar an [] hier sind series Angegeben.
# !!!Diese Listen werden später in ein Pandas-DataFrame umgewandelt.
tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
temperaturen = [10, 12, 15, 14, 13, 11, 9]
monat = ["Januar","Februar","März","April","Mai","Juni","Juli"]  

# !!! WICHTIG: Alle Listen (später Pandas Series) müssen die gleiche Anzahl an Elementen haben,
# da jede Zeile im DataFrame eine vollständige Datenreihe darstellt.

# DataFrame erstellen !!! auch hier kein Array sondern ein DataFrame
df = pd.DataFrame({"Tag": tage, "Monat" : monat ,"Temperatur": temperaturen})

# DataFrame ausgeben
print(df)
print() #Leere Zeile für Übersicht
