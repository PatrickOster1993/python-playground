import numpy as np
import pandas as pd
import tabulate
import matplotlib.pyplot as plt

print(pd.__version__)
tempdata = {
"Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
"Temperaturen": [28, 30, 31.5, 27, 26, 32, 28],
}

temp = pd.DataFrame(tempdata)

plt.plot(temp["Tage"], temp["Temperaturen"], marker='*', linestyle='-', color='black', label='Temperature')


plt.xlabel("Day of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variation Over the Week")

# Toon de legenda
plt.legend()

# Toon het diagram
plt.grid(True)  # Optioneel: raster toevoegen
plt.show()