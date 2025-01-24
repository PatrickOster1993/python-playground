import matplotlib.pyplot as plt

def plot_weather(df, city):
    if not df.empty:
        plt.figure(figsize=(10, 5))
        plt.plot(df['Datum'], df['Maximale Temperatur (°C)'], marker='o', label=city)
        plt.title(f'Maximale Temperaturen in {city}')
        plt.xlabel('Datum')
        plt.ylabel('Maximale Temperatur (°C)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("Keine Daten zum Plotten verfügbar.")