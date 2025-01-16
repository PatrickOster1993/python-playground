import numpy as np

temperatures = np.array([12, 15, 14, 10, 9, 13, 11])

average_temperature = np.mean(temperatures) 
max_temperature = np.max(temperatures)
min_temperature = np.min(temperatures)

print(f"Durchschnittliche Temperatur: {average_temperature} °C")
print(f"Maximale Temperatur: {max_temperature} °C")
print(f"Minimale Temperatur: {min_temperature} °C")
