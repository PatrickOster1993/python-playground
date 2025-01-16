import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

KW1 = np.random.randint(-10, 35, 7)
KW2 = np.random.randint(-10, 35, 7)
KW3 = np.random.randint(-10, 35, 7)
KW4 = np.random.randint(-10, 35, 7)
KW5 = np.random.randint(-10, 35, 7)
KW6 = np.random.randint(-10, 35, 7)
KW7 = np.random.randint(-10, 35, 7)
KW8 = np.random.randint(-10, 35, 7)
KW9 = np.random.randint(-10, 35, 7)
KW10 = np.random.randint(-10, 35, 7)

Temp10W = np.vstack([KW1, KW2, KW3, KW4, KW5, KW6, KW7, KW8, KW9, KW10])
tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

# df = pd.DataFrame({
#     "Tag": tage,
#     "Temperatur": Temp10W
# })

# print(df)
durchschnittTemp = Temp10W.mean(axis=0)

print(durchschnittTemp)
