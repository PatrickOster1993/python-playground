import numpy as np

tempList = np.array([12, 15, 14, 10, 9, 13, 11])

avgTemp =  np.mean(tempList)
maxTemp = np.max(tempList)
minTemp = np.min(tempList)

print(f"Durchsnitt von diesen traumhaften Temperaturen ist ein angenehme {avgTemp} Grad.")
print(f"Maximale Temperatur war {maxTemp} Grad.")
print(f"Minimale Temperatur war {minTemp} Grad.")