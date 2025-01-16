import pandas as pd

temperatures = [12, 15, 14, 10, 9, 8, 11]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

df = pd.DataFrame({
    "Day": weekdays,
    "Temperature": temperatures
})

print(df)
