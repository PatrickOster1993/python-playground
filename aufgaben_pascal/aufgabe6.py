import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Numpy
numpy_array = np.array([12, 15, 14, 10, 9, 13, 11])
print(numpy_array.max())
print(numpy_array.min())
print(numpy_array.mean())


# Pandas
day = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
data = {
    "Tag": day,
    "Temperatur": numpy_array
}

data_frame = pd.DataFrame(data)
print(data_frame)


  # Extract the date and close price columns
dates = data_frame['Tag']
temps = data_frame['Temperatur']

# Create a line plot
plt.plot(dates, temps)

# Show the plot
plt.show()