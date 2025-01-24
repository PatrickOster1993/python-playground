from weather_client import WeatherClient
from visualization import plot_weather

def main():
    # Instanziieren der WeatherClient-Klasse
    client = WeatherClient()

    # Wetterdaten für Berlin abrufen
    client.fetchData("Berlin")

    # Statuscode und Daten ausgeben
    print(f"Statuscode: {client.status}")
    print(f"Daten im Dictionary-Format: {client.dataDict}")

    # Wetterdaten in der Konsole anzeigen
    client.showWeather()

    # DataFrame erstellen und die ersten Zeilen ausgeben
    df = client.dataFrame
    print("\nDataFrame:")
    print(df.head())

    # Wetterdaten visualisieren
    client.plotWeather()

    # Optional: Diagramm speichern
    if not df.empty:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.plot(df['Datum'], df['Maximale Temperatur (°C)'], marker='o')
        plt.title('Maximale Temperaturen in Berlin')
        plt.xlabel('Datum')
        plt.ylabel('Maximale Temperatur (°C)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('weather_berlin.png')
        print("Diagramm wurde als 'weather_berlin.png' gespeichert.")

if __name__ == "__main__":
    main()