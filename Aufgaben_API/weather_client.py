import requests
import pandas as pd

class WeatherClient:
    def __init__(self):
        self._data = None
        self._status = None

    def fetchData(self, city):
        # Beispiel-API-URL für Berlin
        url = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max&timezone=auto"
        response = requests.get(url)
        self._status = response.status_code
        if response.status_code == 200:
            self._data = response.json()
        else:
            print(f"Fehler bei der Anfrage: Statuscode {response.status_code}")

    @property
    def dataDict(self):
        return self._data

    @property
    def status(self):
        return self._status

    def showWeather(self):
        if self._data:
            daily_data = self._data.get('daily', {})
            times = daily_data.get('time', [])
            temps = daily_data.get('temperature_2m_max', [])
            for time, temp in zip(times, temps):
                print(f"{time}: {temp}°C")
        else:
            print("Keine Daten verfügbar.")

    @property
    def dataFrame(self):
        if self._data:
            daily_data = self._data.get('daily', {})
            return pd.DataFrame({
                'Datum': daily_data.get('time', []),
                'Maximale Temperatur (°C)': daily_data.get('temperature_2m_max', [])
            })
        else:
            return pd.DataFrame()

    def plotWeather(self):
        if self._data:
            df = self.dataFrame
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
                plt.show()
            else:
                print("Keine Daten zum Plotten verfügbar.")
        else:
            print("Keine Daten zum Plotten verfügbar.")