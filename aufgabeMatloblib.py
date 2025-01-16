import matplotlib.pyplot as plt

# Deaktiviere den interaktiven Modus
plt.ioff()



plt.xlabel("Temperaturen der Woche")

names = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
values = [12, 15, 14, 10, 9, 13, 11]

# Erstelle das Diagramm
plt.plot(names, values)

# Zeige das Diagramm an
plt.show()

