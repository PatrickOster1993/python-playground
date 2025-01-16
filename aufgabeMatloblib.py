#3. Matplotlib:
#Erstelle ein einfaches Liniendiagramm, das die Temperatur über die Tage darstellt.
#Beschrifte die Achsen:
#x-Achse: Wochentage.
#y-Achse: Temperatur (°C).
#Gib dem Diagramm einen Titel, z. B. "Temperaturen der Woche".
#Füge eine horizontale Linie in das Diagramm ein, die den Durchschnitt der Temperaturen darstellt.
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar


import matplotlib.pyplot as plt

# Deaktiviere den interaktiven Modus
plt.ioff()


plt.title("Temperaturanalyse")
plt.ylabel("Temperatur in Celsius")
plt.xlabel("Mo-So")


names = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
values = [12, 15, 14, 10, 9, 13, 11]

# Erstelle das Diagramm
plt.plot(names, values)

# Zeige das Diagramm an
plt.show()

