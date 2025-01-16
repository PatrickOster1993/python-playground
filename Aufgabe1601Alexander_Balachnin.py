import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Umwandlung der Liste in ein NumPy-Array
temperaturen_arrayKW01 = np.array([12, 15, 14, 10, 9, 13, 11])
temperaturen_arrayKW02 = np.array([20, 30, 10, 15, 8 , 12, 22])
temperaturen_arrayKW03 = np.array([25, 7, 18, 25, 14, 37, 7])
temperaturen_arrayKW04 = np.array([8, 9, 5, 4, 10, 13, 9])
temperaturen_arrayKW05 = np.array([25, 17, 18, 61, 32, 25, 18])
temperaturen_arrayKW06 = np.array([25, 32, 14, 24, 16, 17, 21])
temperaturen_arrayKW07 = np.array([22, 23, 14, 18, 14, 9, 4])
temperaturen_arrayKW08 = np.array([5, 9, 12, 18, 22, 17, 18])
temperaturen_arrayKW09 = np.array([22, 28, 24, 20 , 18, 17, 24])
temperaturen_arrayKW10 = np.array([13, 15, 18, 22, 14, 7, 10])

durchschnittMO = np.mean([
    temperaturen_arrayKW01[0], 
    temperaturen_arrayKW02[0], 
    temperaturen_arrayKW03[0], 
    temperaturen_arrayKW04[0], 
    temperaturen_arrayKW05[0], 
    temperaturen_arrayKW06[0], 
    temperaturen_arrayKW07[0], 
    temperaturen_arrayKW08[0], 
    temperaturen_arrayKW09[0], 
    temperaturen_arrayKW10[0]
    ])
print("durchschnitt Montag:", durchschnittMO)

durchschnittDI = np.mean([
    temperaturen_arrayKW01[1], 
    temperaturen_arrayKW02[1], 
    temperaturen_arrayKW03[1], 
    temperaturen_arrayKW04[1], 
    temperaturen_arrayKW05[1], 
    temperaturen_arrayKW06[1], 
    temperaturen_arrayKW07[1], 
    temperaturen_arrayKW08[1], 
    temperaturen_arrayKW09[1], 
    temperaturen_arrayKW10[1]
    ])
print("durchschnitt Dienstag:", durchschnittDI)

durchschnittMI = np.mean([
    temperaturen_arrayKW01[2], 
    temperaturen_arrayKW02[2], 
    temperaturen_arrayKW03[2], 
    temperaturen_arrayKW04[2], 
    temperaturen_arrayKW05[2], 
    temperaturen_arrayKW06[2], 
    temperaturen_arrayKW07[2], 
    temperaturen_arrayKW08[2], 
    temperaturen_arrayKW09[2], 
    temperaturen_arrayKW10[2]
    ])
print("durchschnitt Mittwoch:", durchschnittMI)

durchschnittDO = np.mean([
    temperaturen_arrayKW01[3], 
    temperaturen_arrayKW02[3], 
    temperaturen_arrayKW03[3], 
    temperaturen_arrayKW04[3], 
    temperaturen_arrayKW05[3], 
    temperaturen_arrayKW06[3], 
    temperaturen_arrayKW07[3], 
    temperaturen_arrayKW08[3], 
    temperaturen_arrayKW09[3], 
    temperaturen_arrayKW10[3]
    ])
print("durchschnitt Donnerstag:", durchschnittDO)

durchschnittFR = np.mean([
    temperaturen_arrayKW01[4], 
    temperaturen_arrayKW02[4], 
    temperaturen_arrayKW03[4], 
    temperaturen_arrayKW04[4], 
    temperaturen_arrayKW05[4], 
    temperaturen_arrayKW06[4], 
    temperaturen_arrayKW07[4], 
    temperaturen_arrayKW08[4], 
    temperaturen_arrayKW09[4], 
    temperaturen_arrayKW10[4]
    ])
print("durchschnitt Freitag:", durchschnittFR)

durchschnittSA = np.mean([
    temperaturen_arrayKW01[5], 
    temperaturen_arrayKW02[5], 
    temperaturen_arrayKW03[5], 
    temperaturen_arrayKW04[5], 
    temperaturen_arrayKW05[5], 
    temperaturen_arrayKW06[5], 
    temperaturen_arrayKW07[5], 
    temperaturen_arrayKW08[5], 
    temperaturen_arrayKW09[5], 
    temperaturen_arrayKW10[5]
    ])
print("durchschnitt Samstag:", durchschnittSA)

durchschnittSO = np.mean([
    temperaturen_arrayKW01[6], 
    temperaturen_arrayKW02[6], 
    temperaturen_arrayKW03[6], 
    temperaturen_arrayKW04[6], 
    temperaturen_arrayKW05[6], 
    temperaturen_arrayKW06[6], 
    temperaturen_arrayKW07[6], 
    temperaturen_arrayKW08[6], 
    temperaturen_arrayKW09[6], 
    temperaturen_arrayKW10[6]
    ])
print("durchschnitt Sonntag:", durchschnittSO)


maximalwert = np.max([
    temperaturen_arrayKW01, 
    temperaturen_arrayKW02, 
    temperaturen_arrayKW03, 
    temperaturen_arrayKW04, 
    temperaturen_arrayKW05, 
    temperaturen_arrayKW06, 
    temperaturen_arrayKW07, 
    temperaturen_arrayKW08, 
    temperaturen_arrayKW09, 
    temperaturen_arrayKW10
    ])
minimalwert = np.min([
    temperaturen_arrayKW01, 
    temperaturen_arrayKW02, 
    temperaturen_arrayKW03, 
    temperaturen_arrayKW04, 
    temperaturen_arrayKW05, 
    temperaturen_arrayKW06, 
    temperaturen_arrayKW07, 
    temperaturen_arrayKW08, 
    temperaturen_arrayKW09, 
    temperaturen_arrayKW10
    ])

temperaturen_arrayDurch = np.array([
    durchschnittMO, 
    durchschnittDI, 
    durchschnittMI, 
    durchschnittDO, 
    durchschnittFR, 
    durchschnittSA, 
    durchschnittSO
    ])


TempDaten = {
    "Tag": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
    "Durchschnittstemperatur": temperaturen_arrayDurch
}

# Erstellen des DataFrames aus dem Dictionary
df = pd.DataFrame(TempDaten)

print(df)



# Erstellen des Liniendiagramms
plt.plot(df.Tag, df.Durchschnittstemperatur, marker='o', linestyle='-', color='blue')

# Beschriftungen
plt.xlabel("Wochentage")
plt.ylabel("Durchschnittstemperatur (°C)")
plt.title("Temperaturen der Woche")

# Diagramm anzeigen
plt.show()