import numpy as np
import pandas as pd
import tabulate
import matplotlib.pyplot as plt
import Numpy1

tempdata = {
"Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
"Temperaturen": [12, 15, 14, 10, 9, 13, 11],
}

avgerage_temp = Numpy1.avgTemp
temp = pd.DataFrame(tempdata)

""" print(tabulate.tabulate(temp))
"""

plt.style.use('dark_background')
plt.plot(temp["Tage"], temp["Temperaturen"], marker='*', linestyle=':', color='red', label='Temperature')
# plt.plot(temp["Tage"], avgerage_temp, marker='*', linestyle='-', color='blue', label='Average Temperature')


plt.xlabel("Day of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variation Over the Week")

# Toon de legenda
plt.legend()

# Toon het diagram
# plt.grid(True)  # Optioneel: raster toevoegen
plt.show()