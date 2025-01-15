import numpy as np

tempList = [28, 30, 31.5, 27, 26, 32, 28, 29, 28, 31]

avgTemp =  np.mean(tempList)
maxTemp = np.max(tempList)
minTemp = np.min(tempList)

print(f"Durchsnitt von diesen traumhaften Temperaturen ist ein angenehme {avgTemp} Grad.")
print(f"Maximale Temperatur war {maxTemp} Grad.")
print(f"Minimale Temperatur war {minTemp} Grad.")