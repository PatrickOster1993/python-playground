import numpy as np

tempList = [28, 30, 31.5, 27, 26, 32, 28, 29, 28, 31]

avgTemp =  np.mean(tempList)
maxTemp = np.max(tempList)
minTemp = np.min(tempList)

print(f"Durchsnitt von diesen traumhaften Temperaturen ist ein angenehmos {avgTemp} Grados")
print(f"Das heisseste neben natürlich Roy ist den Tag das es {maxTemp} war.")
print(f"Das coolste neben Matthias ist den Tag das es {minTemp} war.")