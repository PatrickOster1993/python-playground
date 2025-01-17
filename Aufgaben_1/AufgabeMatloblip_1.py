import matplotlib.pyplot as plt
import numpy as np

plt.ioff()

plt.title("Temperaturanalyse")
plt.ylabel("Temperatur in Celsius")
plt.xlabel("Mo-So")

names = np.array(["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"])
values = np.array([12, 15, 14, 10, 9, 13, 11])


min_temp = values.min()
max_temp = values.max()
mean_temp = values.mean()

print("Die niedrigste Temperatur beträgt: ", min_temp, "°C")
print("Die maximale Temperatur beträgt: ", max_temp, "°C")
print("Die durchschnittliche Temperatur beträgt: ", mean_temp, "°C")

plt.plot(names, values, label="Tägliche Temperaturen",)
plt.axhline(max_temp, label="Maximale Temperatur")

plt.legend()

plt.show()
