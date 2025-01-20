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

plt.plot(names, values, label="Tägliche Temperaturen", marker='o')

plt.plot(names, [min_temp] * len(names), label=f"Min Temperatur: {min_temp}°C", linestyle='--', color='red')

plt.plot(names, [max_temp] * len(names), label=f"Max Temperatur: {max_temp}°C", linestyle=':', color='green')

plt.plot(names, [mean_temp] * len(names), label=f"Durchschnitt: {mean_temp}°C", linestyle='-', color='blue')

plt.legend()

plt.show()
