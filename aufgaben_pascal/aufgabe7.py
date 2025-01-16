import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Numpy
numpy_array = np.array([12, 15, 14, 10, 9, 13, 11])
max_temp = numpy_array.max()
min_temp = numpy_array.min()
avg_temp = numpy_array.mean()

print(f"Max. Temperatur: {max_temp}°C, Min. Temperatur: {min_temp}°C, Durchschnittstemperatur: {avg_temp}°C")

temperatures_random = np.random.randint(0, 20, size=(10, 7))
max_temp_random = temperatures_random.max()
min_temp_random = temperatures_random.min()
avg_temp_random = temperatures_random.mean()


# Selbständige Aufgabe (16. Januar):
# ----------------------------------
# - Nehmen Sie erneut Aufgabe 7 zur Hand und ändern Sie die Lösung dahingehend ab, dass es als "kleines" Vorhersagemodell dient!
# - Erstellen Sie sich hierzu zunächst einmal arrays (geeigneter Datentyp?) für die letzten 10 Kalenderwochen (Temperaturdaten von Mo - So)
# - Berechnen Sie dann die Durchschnittstemperatur für jeden Wochentag über die letzten 10 Wochentag
# - Bestimmen Sie den Höchst- und Tiefstand der Temperatur (wie gehabt)
# - Plotten Sie die Durchschnittstemperatur (y-Achse) über die Wochentage (x-Achse)
# - Fügen Sie noch den Höchst- und Tiefstand in das Diagramm ein 
# - Machen Sie das Diagramm ein klein wenig hübscher:)

# Pandas
day = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
data = {
    "Tag": day,
    "Temperatur": temperatures_random
}

data_frame = pd.DataFrame(data)
print(data_frame)


  # Extract the date and close price columns
dates = data_frame['Tag']
temps = data_frame['Temperatur']

# Create a line plot
plt.plot(data_frame['Tag'], data_frame['Temperatur'], label='Temperatur')
plt.axhline(max_temp_random, color='r', linestyle='--', label='Durchschnittstemperatur')

# Hinzufügen der Legende
plt.legend()

# Show the plot
plt.show()